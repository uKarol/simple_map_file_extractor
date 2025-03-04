#ifndef __BUFFER_CONFIG_H__
#define __BUFFER_CONFIG_H__

#define MAX_BUFFER_SIZE 256
#define MAX_BUFFER_NUMBER 2

#include "stdint.h"

uint32_t __get_IPSR();
void transmit_function(uint8_t *data, uint16_t size);

#endif