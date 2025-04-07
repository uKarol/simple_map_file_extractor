/*
 * revember_user_functions.h
 *
 *  Created on: Apr 7, 2025
 *      Author: Karol
 */

#ifndef REVEMBER_LOGGER_REVEMBER_USER_FUNCTIONS_H_
#define REVEMBER_LOGGER_REVEMBER_USER_FUNCTIONS_H_

#include "revember_logger.h"

#define REVEMBER_FUNCTION_ENTRY_USER() revember_send_text_auto(__FILE__, sizeof(__FILE__)-1);


#endif /* REVEMBER_LOGGER_REVEMBER_USER_FUNCTIONS_H_ */
