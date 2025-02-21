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
#include "string.h"
#include <stdarg.h>
#include "revEMBer_buffer.h"

#define SYNC_SIZE 1U
#define SCENARIO_SIZE 2U
#define PARAM_SIZE 2U
#define DATA_SIZE 2U
#define SYNC_BYTE 0x55U

#define SCENARIO_OFFSET SYNC_SIZE
#define PARAM_OFFSET (SCENARIO_OFFSET + SCENARIO_SIZE)
#define DATA_SIZE_OFFSET (PARAM_OFFSET + PARAM_SIZE)

#define INFO_FRAME_SIZE (DATA_SIZE_OFFSET + DATA_SIZE)

#define MAX_BUFFER_SIZE 200
#define WSEQ_UNIT_SIZE 5
#define ID_SIZE 1



typedef enum
{
	TRANSMIT_INTERFACE_ACTIVE,
	TRANSMIT_INTERFACE_INACTIVE,
}transmit_interface_status_t;

typedef enum
{
	REVEMBER_LOGGERR_INITIALIZED,
	REVEMBER_LOGGER_NOT_INITIALIZED,
}revember_init_status_t;

static volatile revember_init_status_t revember_init_status = REVEMBER_LOGGER_NOT_INITIALIZED;
static volatile transmit_interface_status_t transmit_interface_status = TRANSMIT_INTERFACE_INACTIVE;

static revember_buffer *logging_buffer;
static tx_function logging_tx_fun;

void revember_logger_init(tx_function tx_function_f)
{
	buffer_init(&logging_buffer);
	logging_tx_fun = tx_function_f;
}

void revEMBer_send_bytes(uint8_t *bytes_to_send, uint16_t size)
{
	if(transmit_interface_status == TRANSMIT_INTERFACE_ACTIVE)
	{
		logging_tx_fun(bytes_to_send, size);
	}
	else
	{
		buffer_put(logging_buffer, bytes_to_send, size);
	}
}

void transimt_buffer_flush()
{
	uint8_t temp_buff[MAX_BUFFER_SIZE];
	uint16_t size = buffer_get_size(logging_buffer);
	buffer_get(logging_buffer, temp_buff, size);
	logging_tx_fun(temp_buff, size);
}

void revEMBer_transmit_interface_active()
{
	transmit_interface_status = TRANSMIT_INTERFACE_ACTIVE;
}

void revEMBer_transmit_interface_inactive()
{
	transmit_interface_status = TRANSMIT_INTERFACE_INACTIVE;
}

void revEMBer_WSEQ(uint8_t arg_num, uint16_t scenario_id, ...)
{
    uint8_t revEMBer_buffer[100] = {0};
    va_list list;
    revEMBer_send_info_frame(scenario_id, WSEQ_MESSAGE, arg_num*WSEQ_UNIT_SIZE);
    va_start(list, scenario_id);
    for(int i = 0; i< arg_num; i++)
    {
    	uint8_t param = va_arg(list, int);
        revEMBer_buffer[i*WSEQ_UNIT_SIZE] = param;
        uint32_t value =  va_arg(list, uint32_t);
        memcpy(&(revEMBer_buffer[i*WSEQ_UNIT_SIZE+ID_SIZE]), &value, 4);
    }
    va_end(list);
    revEMBer_send_bytes(revEMBer_buffer, arg_num*WSEQ_UNIT_SIZE);
}



void revEMBer_send_info_frame(uint16_t scenario, uint16_t msg_type, uint16_t size)
{
	uint8_t sync_byte = SYNC_BYTE;
	uint8_t revEMBer_buffer[MAX_BUFFER_SIZE];
	memcpy(revEMBer_buffer, &(sync_byte), SYNC_SIZE);
	memcpy(revEMBer_buffer + SCENARIO_OFFSET, &scenario, SCENARIO_SIZE);
	memcpy(revEMBer_buffer + PARAM_OFFSET, &msg_type, PARAM_SIZE);
	memcpy(revEMBer_buffer + DATA_SIZE_OFFSET, &size, DATA_SIZE);
	revEMBer_send_bytes(revEMBer_buffer, INFO_FRAME_SIZE);
}

//void revEMBer_send_text(uint16_t scenario, uint8_t *text, uint8_t size)
//{
//	uint8_t revEMBer_buffer[MAX_BUFFER_SIZE];
//	revEMBer_send_info_frame(scenario, GENERIC_TEXT_MESSAGE, size);
//	memcpy(revEMBer_buffer, text, size);
//	TRANSMIT_FUNCTION(revEMBer_buffer, size);
//}
