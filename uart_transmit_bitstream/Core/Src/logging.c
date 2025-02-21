/*
 * logging.c
 *
 *  Created on: Feb 5, 2025
 *      Author: karol
 */
//#include "logging.h"
//#include "logging_conf.h"
//#include "string.h"
//#include <stdarg.h>
//
//#define SYNC_SIZE 1U
//#define SCENARIO_SIZE 2U
//#define PARAM_SIZE 2U
//#define DATA_SIZE 2U
//#define SYNC_BYTE 0x55U
//
//#define SCENARIO_OFFSET SYNC_SIZE
//#define PARAM_OFFSET (SCENARIO_OFFSET + SCENARIO_SIZE)
//#define DATA_SIZE_OFFSET (PARAM_OFFSET + PARAM_SIZE)
//
//#define INFO_FRAME_SIZE (DATA_SIZE_OFFSET + DATA_SIZE)
//
//#define MAX_BUFFER_SIZE 200
//#define DMSK_UNIT_SIZE 5
//#define ID_SIZE 1
//
//void logging_DMSK(uint8_t arg_num, uint16_t scenario_id, ...)
//{
//    uint8_t logging_buffer[100] = {0};
//    va_list list;
//    logging_send_info_frame(scenario_id, DMSK_MESSAGE, arg_num*DMSK_UNIT_SIZE);
//    va_start(list, scenario_id);
//    for(int i = 0; i< arg_num; i++)
//    {
//    	uint8_t param = va_arg(list, int);
//        logging_buffer[i*DMSK_UNIT_SIZE] = param;
//        uint32_t value =  va_arg(list, uint32_t);
//        memcpy(&(logging_buffer[i*DMSK_UNIT_SIZE+ID_SIZE]), &value, 4);
//    }
//    va_end(list);
//    TRANSMIT_FUNCTION(logging_buffer, arg_num*DMSK_UNIT_SIZE);
//    //print_array(logging_buffer, arg_num*UNIT_SIZE);
//}
//
//void logging_experimental()
//{
//	uint8_t buffer[20] = { 0x1, 0x22, 0x33, 0x44, 0x55,
//						   0x2, 0xAA, 0xBB, 0xCC, 0xDD,
//						   0x3, 0x55, 0x11, 0x88, 0x00,
//						   0x4, 0xAA, 0x40, 0xCC, 0xEE,};
//	TRANSMIT_FUNCTION(buffer, 20);
//}
//
//
//
//void logging_send_pointer(uint16_t scenario, void *ptr)
//{
//	uint8_t logging_buffer[MAX_LOGGING_BUFFER];
//	uint32_t value = (uint32_t)ptr;
//	logging_send_info_frame(scenario, POINTER_DECODE, sizeof(void*));
//	memcpy(logging_buffer, (uint8_t*)&value, sizeof(void*));
//	TRANSMIT_FUNCTION(logging_buffer, sizeof(void*));
//}
//
//void logging_send_info_frame(uint16_t scenario, uint16_t msg_type, uint16_t size)
//{
//	uint8_t sync_byte = SYNC_BYTE;
//	uint8_t logging_buffer[MAX_LOGGING_BUFFER];
//	memcpy(logging_buffer, &(sync_byte), SYNC_SIZE);
//	memcpy(logging_buffer + SCENARIO_OFFSET, &scenario, SCENARIO_SIZE);
//	memcpy(logging_buffer + PARAM_OFFSET, &msg_type, PARAM_SIZE);
//	memcpy(logging_buffer + DATA_SIZE_OFFSET, &size, DATA_SIZE);
//	TRANSMIT_FUNCTION(logging_buffer, INFO_FRAME_SIZE);
//}
//
//void logging_send_text(uint16_t scenario, uint8_t *text, uint8_t size)
//{
//	uint8_t logging_buffer[MAX_LOGGING_BUFFER];
//	logging_send_info_frame(scenario, GENERIC_TEXT_MESSAGE, size);
//	memcpy(logging_buffer, text, size);
//	TRANSMIT_FUNCTION(logging_buffer, size);
//}
