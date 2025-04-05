/*
 * logginh_conf.h
 *
 *  Created on: Feb 5, 2025
 *      Author: karol
 */

#ifndef INC_LOGGING_CONF_H_
#define INC_LOGGING_CONF_H_

#define MAX_LOGGING_BUFFER 100	/* logging buffer size in bytes */

#include "stm32g4xx_nucleo.h"

#define TRANSMIT_FUNCTION(DATA, SIZE) HAL_UART_Transmit(hcom_uart, DATA, SIZE, 100);

#endif /* INC_LOGGING_CONF_H_ */
