/*
 * logging.h
 *
 *  Created on: Feb 5, 2025
 *      Author: karol
 */

#ifndef INC_LOGGING_H_
#define INC_LOGGING_H_

#include <stdint.h>

//#define REVEMBER_FUNCTION_ENTRY() \
//		{							\
//		uint32_t temp_lr = 0;\
//		uint32_t temp_pc = 0;\
//		asm volatile(\
//			"mov %[lr_destination], lr \n\t"\
//			"mov %[pc_destination], pc \n\t"\
//			:[lr_destination] "=r" (temp_lr), [pc_destination] "=r" (temp_pc)\
//			:\
//			:"memory");\
//		logging_DMSK(2, 0, FUNCTION_ENTRY, temp_pc, LINK_REGISTER, temp_lr);\
//		}
//
//#define REVEMBER_FUNCTION_EXIT()\
//		{\
//			uint32_t temp_pc=0;\
//		asm volatile(\
//			"mov %[destination], pc \n\t"\
//			:[destination] "=r" (temp_pc)\
//			:\
//			:"memory");\
//		logging_DMSK(1, 0, FUNCTION_EXIT, temp_pc);\
//		}
//
//
//typedef enum
//{
//	GENERIC_TEXT_MESSAGE,
//	LINK_REG_DECODE,
//	POINTER_DECODE,
//};
//
//typedef enum
//{
//	TEXT_MESSAGE = 0,
//	DMSK_MESSAGE,
//	MEMORY_DUMP_MESSAGE,
//};
//
//typedef enum
//{
//	FUNCTION_ENTRY = 0,
//	FUNCTION_EXIT,
//	FUNCTION_RETURN,
//	LINK_REGISTER,
//	FUNCTION_POINTER,
//	VARIABLE_POINTER,
//}DMSK_params;
//
//typedef enum
//{
//	SCENARION_DBG_0,
//};
//
//typedef struct
//{
//	uint8_t sync;
//	uint16_t scenario;
//	uint16_t param;
//	uint16_t size;
//} logging_struct;
//
//void logging_DMSK(uint8_t arg_num, uint16_t scenario_id, ...);
//void logging_send_info_frame(uint16_t scenario, uint16_t message_type, uint16_t size);
//void logging_send_pointer(uint16_t scenario, void *ptr);
//void logging_send_text(uint16_t scenario, uint8_t *text, uint8_t size);
//void logging_experimental();
#endif /* INC_LOGGING_H_ */
