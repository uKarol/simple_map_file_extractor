/*
 * revEMBer_buffer.c
 *
 *  Created on: Feb 21, 2025
 *      Author: karol
 */


#include "revember_buffer.h"
#include "buffer_config.h"

#ifndef TEST
	#define PRIVATE_OBJ static
#else
	#define PRIVATE_OBJ
#endif



PRIVATE_OBJ uint8_t buffer_array[MAX_BUFFER_NUMBER][MAX_BUFFER_SIZE];
PRIVATE_OBJ revember_buffer my_buffer[MAX_BUFFER_NUMBER];
PRIVATE_OBJ uint8_t allocated_buffer_count = 0;

/**
 *
 */
buffer_status_t buffer_init(revember_buffer **buffer)
{   
    buffer_status_t ret_val;
    if(allocated_buffer_count == MAX_BUFFER_NUMBER)
    {
        *buffer = NULL;
        ret_val = BUFFER_ERROR;
    }
    else
    {
        *buffer = &(my_buffer[allocated_buffer_count]);
        (*buffer)->buffer = buffer_array[allocated_buffer_count];
        (*buffer)->element_number = 0;
        (*buffer)->head_ptr = 0;
        (*buffer)->tail_ptr = 0;
        allocated_buffer_count++;
        ret_val = BUFFER_OK;
    }
    return ret_val;
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
    if(buffer->element_number + size <= MAX_BUFFER_SIZE)
    {
        for(uint32_t i = 0; i < size; i++)
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

uint32_t buffer_get_size(revember_buffer *buffer)
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
        for(uint32_t i = 0; i < size; i++)
        {
            data[i] = buffer->buffer[buffer->head_ptr];
            buffer->element_number--;
            buffer->head_ptr = (buffer->head_ptr + 1) % MAX_BUFFER_SIZE;
        }
        ret_val = BUFFER_OK;
    }
    else
    {
        ret_val = BUFFER_EMPTY;
    }
    return ret_val;
}
