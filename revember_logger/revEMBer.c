/*
 * revEMBer.c
 *
 *  Created on: Feb 5, 2025
 *      Author: karol
 */
#include "revEMBer.h"
#include <string.h>
#include <stdarg.h>
#include "revEMBer_buffer.h"
#include "buffer_config.h"

#ifndef TEST
	#include "cmsis_gcc.h"
#endif

#define SYNC_SIZE 1U
#define SCENARIO_SIZE 2U
#define PARAM_SIZE 2U
#define DATA_SIZE 2U
#define SYNC_BYTE 0x55U

#define SCENARIO_OFFSET SYNC_SIZE
#define PARAM_OFFSET (SCENARIO_OFFSET + SCENARIO_SIZE)
#define DATA_SIZE_OFFSET (PARAM_OFFSET + PARAM_SIZE)

#define HEADER_FRAME_SIZE (DATA_SIZE_OFFSET + DATA_SIZE)


#define WSEQ_UNIT_SIZE 5
#define ID_SIZE 1

#ifndef TEST
	#define PRIVATE_OBJ static
#else
	#define PRIVATE_OBJ
#endif

typedef enum
{
	REVEMBER_LOGGER_NOT_INITIALIZED,
	REVEMBER_LOGGER_ACTIVE,
	REVEMBER_LOGGER_SUSPENDED,
	REVEMBER_LOGGER_ERROR,
}revember_logger_status_t;

typedef enum
{
	DATA_BUFFER_OVERFLOW,
};

PRIVATE_OBJ volatile revember_logger_status_t revember_logger_status = REVEMBER_LOGGER_NOT_INITIALIZED;

PRIVATE_OBJ revember_buffer *data_buffer = NULL;
PRIVATE_OBJ revember_buffer *header_buffer = NULL;
PRIVATE_OBJ tx_function logging_tx_fun = NULL;
PRIVATE_OBJ void revEMBer_prepare_header_frame(uint16_t scenario, uint16_t msg_type, uint16_t size, uint8_t* header_frame);
PRIVATE_OBJ void revember_set_error(uint16_t scenario_id, uint8_t error_code);


PRIVATE_OBJ uint16_t last_scenario_id = 0; 
PRIVATE_OBJ uint16_t last_msg_type = 0;
PRIVATE_OBJ uint16_t last_size = 0;


PRIVATE_OBJ void revember_finish_buffering();

#define ISR_NUM 256
#define MAX_THREAED_NUM 1 /* only main thread */

uint8_t error_buffer[HEADER_FRAME_SIZE+1];

revember_logger_status_t isr_active_tab[ISR_NUM] = {REVEMBER_LOGGER_NOT_INITIALIZED}; 

revember_logger_status_t isr_active_thread_tab[MAX_THREAED_NUM] = {REVEMBER_LOGGER_NOT_INITIALIZED};


PRIVATE_OBJ revember_logger_status_t get_scenario_id(uint16_t *scenario_num)
{
	revember_logger_status_t ret_val = REVEMBER_LOGGER_NOT_INITIALIZED;
	if(REVEMBER_LOGGER_ACTIVE == revember_logger_status)
	{
		uint8_t isr_number = __get_IPSR();
		if(isr_number)
		{
			*scenario_num = isr_number;
			ret_val = isr_active_tab[isr_number];
		}
		else
		{
			*scenario_num = 0;
			ret_val = isr_active_thread_tab[0];
		}
	}
	return ret_val;
}

PRIVATE_OBJ void revEMBer_transmit_bytes(uint8_t *bytes_to_send, uint16_t size)
{
	revember_logger_status_t last_state = revember_logger_status;
	revember_logger_status = REVEMBER_LOGGER_SUSPENDED;
	logging_tx_fun(bytes_to_send, size);
	revember_logger_status = last_state;
}


PRIVATE_OBJ void revember_finish_buffering()
{
	__disable_irq();
	if(last_size > 0)
	{
		uint8_t header_frame[HEADER_FRAME_SIZE];
		revEMBer_prepare_header_frame(last_scenario_id, last_msg_type, last_size, header_frame);
		buffer_put(header_buffer, header_frame, HEADER_FRAME_SIZE);
	}
	last_size = 0;
	last_scenario_id = 0;
	last_msg_type = 0;
	__enable_irq();
}

PRIVATE_OBJ void revEMBer_prepare_header_frame(uint16_t scenario, uint16_t msg_type, uint16_t size, uint8_t* header_frame)
{
	uint8_t sync_byte = SYNC_BYTE;
	memcpy(header_frame, &(sync_byte), SYNC_SIZE);
	memcpy(header_frame + SCENARIO_OFFSET, &scenario, SCENARIO_SIZE);
	memcpy(header_frame + PARAM_OFFSET, &msg_type, PARAM_SIZE);
	memcpy(header_frame + DATA_SIZE_OFFSET, &size, DATA_SIZE);
}

void revember_buffer_frame(uint16_t scenario_id, uint16_t msg_type, uint16_t size, uint8_t* frame, uint8_t disabled_irq)
{
	__disable_irq();
	if(BUFFER_OK == buffer_put(data_buffer, frame, size))
	{
		if((last_scenario_id == scenario_id) && (last_msg_type == msg_type))
		{
			last_size += size;
		}
		else
		{
			if(last_size > 0)
			{
				uint8_t header_frame[HEADER_FRAME_SIZE];
				revEMBer_prepare_header_frame(last_scenario_id, last_msg_type, last_size, header_frame);
				buffer_put(header_buffer, header_frame, HEADER_FRAME_SIZE);
			}
			last_size = size;
			last_scenario_id = scenario_id;
			last_msg_type = msg_type;
		}
	}
	else
	{
		revember_set_error(scenario_id, DATA_BUFFER_OVERFLOW);
	}
	if(disabled_irq == 0)
	{
		__enable_irq();
	}
}


void revEMBer_WSEQ_auto(uint8_t arg_num, ...)
{
	uint16_t scenario_id;
	if((get_scenario_id(&scenario_id) == REVEMBER_LOGGER_ACTIVE) &&
	   (revember_logger_status == REVEMBER_LOGGER_ACTIVE))
	{
		uint8_t revEMBer_buffer[MAX_BUFFER_SIZE] = {0};
		va_list list;
		va_start(list, arg_num);
		for(int i = 0; i< arg_num; i++)
		{
			uint8_t param = va_arg(list, int);
		 	revEMBer_buffer[i*WSEQ_UNIT_SIZE] = param;
			uint32_t value =  va_arg(list, uint32_t);
			memcpy(&(revEMBer_buffer[i*WSEQ_UNIT_SIZE+ID_SIZE]), &value, 4);
		}
		va_end(list);
		revember_buffer_frame(scenario_id, WSEQ_MESSAGE, arg_num*WSEQ_UNIT_SIZE, revEMBer_buffer, __get_PRIMASK());
	}
}

void revEMBer_WSEQ(uint8_t arg_num, uint16_t scenario_id, ...)
{
	if(revember_logger_status == REVEMBER_LOGGER_ACTIVE)
	{
		uint8_t revEMBer_buffer[MAX_BUFFER_SIZE] = {0};
		va_list list;
		
		va_start(list, scenario_id);
		for(int i = 0; i< arg_num; i++)
		{
			uint8_t param = va_arg(list, int);
			revEMBer_buffer[i*WSEQ_UNIT_SIZE] = param;
			uint32_t value =  va_arg(list, uint32_t);
			memcpy(&(revEMBer_buffer[i*WSEQ_UNIT_SIZE+ID_SIZE]), &value, 4);
		}
		va_end(list);

		revember_buffer_frame(scenario_id, WSEQ_MESSAGE, arg_num*WSEQ_UNIT_SIZE, revEMBer_buffer, __get_PRIMASK());
	}
}

void revEMBer_send_text(uint16_t scenario, uint8_t *text, uint8_t size)
{
	if(revember_logger_status == REVEMBER_LOGGER_ACTIVE)
	{
		uint8_t revEMBer_buffer[MAX_BUFFER_SIZE];
		memcpy(revEMBer_buffer, text, size);
		revember_buffer_frame(scenario, TEXT_MESSAGE, size, revEMBer_buffer, __get_PRIMASK());
	}
}

void revEMBer_send_text_auto(uint8_t *text, uint8_t size)
{
	uint16_t scenario_id;
	if((get_scenario_id(&scenario_id) == REVEMBER_LOGGER_ACTIVE) &&
			   (revember_logger_status == REVEMBER_LOGGER_ACTIVE))
	{
		uint8_t revEMBer_buffer[MAX_BUFFER_SIZE];
		memcpy(revEMBer_buffer, text, size);
		revember_buffer_frame(scenario_id, TEXT_MESSAGE, size, revEMBer_buffer, __get_PRIMASK());
	}
}

void transimt_buffer_flush()
{
	if((revember_logger_status == REVEMBER_LOGGER_ACTIVE) || 
		(revember_logger_status == REVEMBER_LOGGER_ERROR))
	{
		revember_finish_buffering();
		uint16_t number_of_frames = buffer_get_size(header_buffer) / HEADER_FRAME_SIZE; 
		for(uint8_t ctr = 0; ctr < number_of_frames; ctr++)
		{
			uint8_t temp_header[HEADER_FRAME_SIZE];
			buffer_get(header_buffer, temp_header, HEADER_FRAME_SIZE);
			revEMBer_transmit_bytes(temp_header, HEADER_FRAME_SIZE);
			uint16_t data_size;
			memcpy((uint8_t*)(&data_size), temp_header + 5, 2);
			

			uint8_t temp_buffer_data[MAX_BUFFER_SIZE];
			buffer_get(data_buffer, temp_buffer_data, data_size);
			revEMBer_transmit_bytes(temp_buffer_data, data_size);
		}
	}
	if(revember_logger_status == REVEMBER_LOGGER_ERROR)
	{
		revEMBer_transmit_bytes(error_buffer, HEADER_FRAME_SIZE+1);
	}
}

void revember_logger_resume()
{
	revember_logger_status = REVEMBER_LOGGER_ACTIVE;
}

void revember_logger_suspend()
{
	revember_logger_status = REVEMBER_LOGGER_SUSPENDED;
}

revEMBer_status_t revember_logger_init(tx_function tx_function_f)
{
	revEMBer_status_t ret_val = REVEMBER_ERROR;
	if((tx_function_f != NULL) && (revember_logger_status == REVEMBER_LOGGER_NOT_INITIALIZED))
	{
		if((BUFFER_OK == buffer_init(&data_buffer)) && 
		(BUFFER_OK == buffer_init(&header_buffer)))
		{
			logging_tx_fun = tx_function_f;
			revember_logger_status = REVEMBER_LOGGER_ACTIVE;
			ret_val = REVEMBER_OK;
		}
	}
	return ret_val;
}

void revember_set_error(uint16_t scenario_id, uint8_t error_code)
{
	revember_logger_status = REVEMBER_LOGGER_ERROR;
	revEMBer_prepare_header_frame(scenario_id, ERROR_MESSAGE, 1, error_buffer);
	error_buffer[HEADER_FRAME_SIZE] = error_code;
	//revember_buffer_frame(scenario_id, ERROR_MESSAGE, 1, &error_code, __get_PRIMASK());
}

void revember_activate_logging_on_isr(uint8_t isr_id)
{
	isr_active_tab[isr_id] = REVEMBER_LOGGER_ACTIVE;
}

void revember_deactivate_logging_on_isr(uint8_t isr_id)
{
	isr_active_tab[isr_id] = REVEMBER_LOGGER_NOT_INITIALIZED;
}

void revember_activate_logging_on_thread(uint8_t thread_id)
{
	if(thread_id < MAX_THREAED_NUM)
	{
		isr_active_thread_tab[thread_id] = REVEMBER_LOGGER_ACTIVE;
	}
}

void revember_deactivate_logging_on_thread(uint8_t thread_id)
{
	if(thread_id < MAX_THREAED_NUM)
	{
		isr_active_thread_tab[thread_id] = REVEMBER_LOGGER_NOT_INITIALIZED;
	}
}
