/*
 * revember_macros.h
 *
 *  Created on: Apr 7, 2025
 *      Author: Karol
 */

#ifndef REVEMBER_LOGGER_REVEMBER_MACROS_H_
#define REVEMBER_LOGGER_REVEMBER_MACROS_H_

#include "revember_user_functions.h"

#ifndef REVEMBER_FUNCTION_ENTRY_USER
#define REVEMBER_FUNCTION_ENTRY_USER()
#endif

#ifndef REVEMBER_FUNCTION_EXIT_USER
#define REVEMBER_FUNCTION_EXIT_USER()
#endif

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
		revember_WSEQ_auto(2, FUNCTION_ENTRY, temp_pc, LINK_REGISTER, temp_lr);\
		REVEMBER_FUNCTION_ENTRY_USER() \
		}

#define REVEMBER_FUNCTION_EXIT()\
		{\
			uint32_t temp_pc=0;\
		asm volatile(\
			"mov %[destination], pc \n\t"\
			:[destination] "=r" (temp_pc)\
			:\
			:"memory");\
		revember_WSEQ_auto(1, FUNCTION_EXIT, temp_pc);\
		REVEMBER_FUNCTION_EXIT_USER() \
		}

#define REVEMBER_FUNCTION_PARAMETERS(PARAM_NUM, ...)\
		{\
			revember_WSEQ_auto(PARAM_NUM, __VA_ARGS__);\
		}

#endif

#endif /* REVEMBER_LOGGER_REVEMBER_MACROS_H_ */
