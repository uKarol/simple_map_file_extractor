/*
 * revember_logger.h
 *
 *  Created on: Apr 7, 2025
 *      Author: Karol
 */

#ifndef REVEMBER_LOGGER_REVEMBER_LOGGER_H_
#define REVEMBER_LOGGER_REVEMBER_LOGGER_H_

#include <stdint.h>


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

/**
 *
 */
revEMBer_status_t revember_logger_init(tx_function tx_function_f);

void revember_deactivate_logging_on_thread(uint8_t thread_id);
void revember_activate_logging_on_thread(uint8_t thread_id);
void revember_deactivate_logging_on_isr(uint8_t isr_id);
void revember_activate_logging_on_isr(uint8_t isr_id);

void revember_WSEQ(uint8_t arg_num, uint16_t scenario_id, ...);
void revember_WSEQ_auto(uint8_t arg_num, ...);

void revember_send_text(uint16_t scenario, uint8_t *text, uint8_t size);
void revember_send_text_auto(uint8_t *text, uint8_t size);

void revember_buffer_flush();

#endif /* REVEMBER_LOGGER_REVEMBER_LOGGER_H_ */
