/*
 * revEMBer_buffer.h
 *
 *  Created on: Feb 21, 2025
 *      Author: karol
 */

#ifndef INC_REVEMBER_BUFFER_H_
#define INC_REVEMBER_BUFFER_H_

#include <stdint.h>
#include <stddef.h>
 //struct revember_buffer revember_buffer;
 typedef struct revember_buffer{
    uint32_t head_ptr;
    uint32_t tail_ptr;
    uint32_t element_number;
    uint8_t *buffer;
}revember_buffer;
typedef enum{
    BUFFER_OK,
    BUFFER_EMPTY,
    BUFFER_BUSY,
    BUFFER_ERROR,
}buffer_status_t;



/**
 *
 */
buffer_status_t buffer_init(revember_buffer **buffer);

/**
 *
 */
buffer_status_t buffer_clear(revember_buffer *buffer);

/**
 *
 */
buffer_status_t buffer_put(revember_buffer *buffer, uint8_t *data, uint16_t size);

/**
 *
 */
buffer_status_t buffer_get(revember_buffer *buffer, uint8_t *data, uint16_t size);

uint32_t buffer_get_size(revember_buffer *buffer);

#endif /* INC_REVEMBER_BUFFER_H_ */
