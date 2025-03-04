/*
 * revEMBer.c
 *
 *  Created on: Feb 20, 2025
 *      Author: karol
 */


/*
 * revEMBer.c
 *
 *  Created on: Feb 5, 2025
 *      Author: karol
 */
#include "revEMBer.h"
//#include "revEMBer_conf.h"
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
	IN_ISR,
	IN_THREAD,
}mcu_mode;

typedef enum
{
	TRANSMIT_INTERFACE_ACTIVE,
	TRANSMIT_INTERFACE_INACTIVE,
}transmit_interface_status_t;

typedef enum
{
	REVEMBER_LOGGER_ACTIVE,
	REVEMBER_LOGGER_NOT_INITIALIZED,
	REVEMBER_LOGGER_SUSPENDED,
}revember_logger_status_t;

PRIVATE_OBJ volatile revember_logger_status_t revember_logger_status = REVEMBER_LOGGER_NOT_INITIALIZED;
PRIVATE_OBJ volatile transmit_interface_status_t transmit_interface_status = TRANSMIT_INTERFACE_INACTIVE;

PRIVATE_OBJ revember_buffer *data_buffer = NULL;
PRIVATE_OBJ revember_buffer *header_buffer = NULL;
PRIVATE_OBJ tx_function logging_tx_fun = NULL;
PRIVATE_OBJ void revEMBer_prepare_header_frame(uint16_t scenario, uint16_t msg_type, uint16_t size, uint8_t* header_frame);
PRIVATE_OBJ mcu_mode revember_check_mcu_mode();

PRIVATE_OBJ uint16_t last_scenario_id = 0; 
PRIVATE_OBJ uint16_t last_msg_type = 0;
PRIVATE_OBJ uint16_t last_size = 0;

void revember_finish_buffering();

mcu_mode revember_check_mcu_mode()
{
	mcu_mode ret_val = IN_THREAD;
	uint32_t psr = __get_IPSR();
	if(psr != 0U)
	{
		ret_val = IN_ISR;
	}
	return ret_val;
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

void revEMBer_transmit_bytes(uint8_t *bytes_to_send, uint16_t size)
{
		revember_logger_status = REVEMBER_LOGGER_SUSPENDED;
		logging_tx_fun(bytes_to_send, size);
		revember_logger_status = REVEMBER_LOGGER_ACTIVE;
}

void transimt_buffer_flush()
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
		revEMBer_transmit_bytes(temp_header, data_size);
	}
}

void revEMBer_transmit_interface_active()
{
	transmit_interface_status = TRANSMIT_INTERFACE_ACTIVE;
}

void revEMBer_transmit_interface_inactive()
{
	transmit_interface_status = TRANSMIT_INTERFACE_INACTIVE;
}

uint8_t transmission_possible()
{
	uint8_t ret_val = 0;
	if((transmit_interface_status == TRANSMIT_INTERFACE_ACTIVE) && 
		(revember_check_mcu_mode() == IN_THREAD))
	{
		ret_val = 1;
	}
	return ret_val;
 }

 void revember_finish_buffering()
 {
	if(last_size > 0)
	{
		uint8_t header_frame[HEADER_FRAME_SIZE];
		revEMBer_prepare_header_frame(last_scenario_id, last_msg_type, last_size, header_frame);
		buffer_put(header_buffer, header_frame, HEADER_FRAME_SIZE);
	}
	last_size = 0;
	last_scenario_id = 0;
	last_msg_type = 0;
 }

 void revember_buffer_frame(uint16_t scenario_id, uint16_t msg_type, uint16_t size, uint8_t* frame)
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
	buffer_put(data_buffer, frame, size);
 }

 void revember_send_frame(uint16_t scenario_id, uint16_t msg_type, uint16_t size, uint8_t* frame)
 {
	if(transmission_possible())
	{
		uint8_t header_frame[HEADER_FRAME_SIZE];
		revEMBer_prepare_header_frame(scenario_id, msg_type, size, header_frame);
		revEMBer_transmit_bytes(header_frame, HEADER_FRAME_SIZE);
		revEMBer_transmit_bytes(frame, size);
	}
	else
	{
		revember_buffer_frame(scenario_id, msg_type, size, frame);
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

		revember_send_frame(scenario_id, WSEQ_MESSAGE, arg_num*WSEQ_UNIT_SIZE, revEMBer_buffer);
	}
}


void revEMBer_prepare_header_frame(uint16_t scenario, uint16_t msg_type, uint16_t size, uint8_t* header_frame)
{
	uint8_t sync_byte = SYNC_BYTE;
	memcpy(header_frame, &(sync_byte), SYNC_SIZE);
	memcpy(header_frame + SCENARIO_OFFSET, &scenario, SCENARIO_SIZE);
	memcpy(header_frame + PARAM_OFFSET, &msg_type, PARAM_SIZE);
	memcpy(header_frame + DATA_SIZE_OFFSET, &size, DATA_SIZE);
}

//void revEMBer_send_text(uint16_t scenario, uint8_t *text, uint8_t size)
//{
//	uint8_t revEMBer_buffer[MAX_BUFFER_SIZE];
//	revEMBer_send_info_frame(scenario, GENERIC_TEXT_MESSAGE, size);
//	memcpy(revEMBer_buffer, text, size);
//	TRANSMIT_FUNCTION(revEMBer_buffer, size);
//}
