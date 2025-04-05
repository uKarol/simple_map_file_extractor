/*
 * revEMBer.h
 *
 *  Created on: Feb 20, 2025
 *      Author: karol
 */

#ifndef INC_REVEMBER_H_
#define INC_REVEMBER_H_

#include <stdint.h>

#ifndef TEST
#define REVEMBER_FUNCTION_ENTRY() \
		{							\
		uint32_t temp_lr = 0;\
		uint32_t temp_pc = 0;\
		asm volatile(\
			"mov %[lr_destination], lr \n\t"\
			"mov %[pc_destination], pc \n\t"\
			:[lr_destination] "=r" (temp_lr), [pc_destination] "=r" (temp_pc)\
			:\
			:"memory");\
		revEMBer_WSEQ_auto(2, FUNCTION_ENTRY, temp_pc, LINK_REGISTER, temp_lr);\
		}

#define REVEMBER_FUNCTION_EXIT()\
		{\
			uint32_t temp_pc=0;\
		asm volatile(\
			"mov %[destination], pc \n\t"\
			:[destination] "=r" (temp_pc)\
			:\
			:"memory");\
		revEMBer_WSEQ_auto(1, FUNCTION_EXIT, temp_pc);\
		}
#endif
typedef void (*tx_function)(uint8_t *data, uint16_t size);

typedef enum
{
	TEXT_MESSAGE = 0,
	WSEQ_MESSAGE,
	ERROR_MESSAGE,
	MEMORY_DUMP_MESSAGE,

}revEMBer_message_type;

typedef enum
{
	FUNCTION_ENTRY = 0,
	FUNCTION_EXIT,
	FUNCTION_RETURN,
	LINK_REGISTER,
	FUNCTION_POINTER,
	VARIABLE_POINTER,
}WSEQ_params;

typedef enum
{
	SCENARION_DBG_0,
}revEMBer_scenarios_t;

typedef enum
{
	REVEMBER_ERROR,
	REVEMBER_OK,
}revEMBer_status_t;

typedef struct
{
	uint8_t sync;
	uint16_t scenario;
	uint16_t param;
	uint16_t size;
} revEMBer_struct;


revEMBer_status_t revember_logger_init(tx_function tx_function_f);

void revember_deactivate_logging_on_thread(uint8_t thread_id);
void revember_activate_logging_on_thread(uint8_t thread_id);
void revember_deactivate_logging_on_isr(uint8_t isr_id);
void revember_activate_logging_on_isr(uint8_t isr_id);

void revEMBer_WSEQ(uint8_t arg_num, uint16_t scenario_id, ...);
void revEMBer_WSEQ_auto(uint8_t arg_num, ...);

void revEMBer_send_text(uint16_t scenario, uint8_t *text, uint8_t size);
void revEMBer_send_text_auto(uint8_t *text, uint8_t size);

void transimt_buffer_flush();

#endif /* INC_REVEMBER_H_ */
