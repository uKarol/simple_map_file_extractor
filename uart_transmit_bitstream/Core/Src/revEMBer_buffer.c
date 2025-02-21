/*
 * revEMBer_buffer.c
 *
 *  Created on: Feb 21, 2025
 *      Author: karol
 */


#include "revember_buffer.h"
#include "buffer_config.h"

struct revember_buffer{
    uint32_t head_ptr;
    uint32_t tail_ptr;
    uint8_t *buffer;
    uint8_t element_number;
};

static uint8_t buffer_array[MAX_BUFFER_SIZE][MAX_BUFFER_NUMBER];
static revember_buffer my_buffer[MAX_BUFFER_NUMBER];

/**
 *
 */
buffer_status_t buffer_init(revember_buffer **buffer)
{
    *buffer = &(my_buffer[0]);
    my_buffer->buffer = buffer_array[0];
    my_buffer->element_number = 0;
    my_buffer->head_ptr = 0;
    my_buffer->tail_ptr = 0;
    return BUFFER_OK;
}

/**
 *
 */
buffer_status_t buffer_clear(revember_buffer *buffer)
{
    buffer->head_ptr = 0;
    buffer->tail_ptr = 0;
    buffer->element_number = 0;
    return BUFFER_OK;
}

/**
 *
 */
buffer_status_t buffer_put(revember_buffer *buffer, uint8_t *data, uint16_t size)
{
    buffer_status_t ret_val;
    if(buffer->element_number + size < MAX_BUFFER_SIZE)
    {
        for(uint16_t i = 0; i < size; i++)
        {
            buffer->buffer[buffer->tail_ptr] = data[i];
            buffer->element_number++;
            buffer->tail_ptr = (buffer->tail_ptr + 1) % MAX_BUFFER_SIZE;
        }
        ret_val = BUFFER_OK;
    }
    else
    {
        ret_val = BUFFER_BUSY;
    }
    return ret_val;
}

uint16_t buffer_get_size(revember_buffer *buffer)
{
    return buffer->element_number;
}

/**
 *
 */
buffer_status_t buffer_get(revember_buffer *buffer, uint8_t *data, uint16_t size)
{
    buffer_status_t ret_val;
    if(buffer->element_number >= size)
    {
        for(uint16_t i = 0; i < size; i++)
        {
            data[i] = buffer->buffer[buffer->head_ptr];
            buffer->element_number--;
            buffer->head_ptr = (buffer->head_ptr + 1) % MAX_BUFFER_SIZE;
        }
        ret_val = BUFFER_OK;
    }
    else
    {
        ret_val = BUFFER_BUSY;
    }
    return ret_val;
}
