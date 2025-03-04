
#define TEST
#ifdef TEST

#include "unity.h"

#include "revEMBer.h"
#include "revEMBer_buffer.h"
#include "mock_buffer_config.h"
#include <string.h>
#include <stdint.h>
#include <stdio.h>

char vatras_monolog[] = "Ale Beliar nie znosil widoku swiatla i niszczyl wszystko, co Innos stworzyl.\
Ujrzal wtedy Adanos, ze w ten sposob nic nie moze istniec na swiecie – ani jasnosc, ani mrok.\
Stanal wiec miedzy swymi bracmi i probowal pojednac ich miedzy soba… jednakze bez skutku.\
Ale tam, gdzie stanal Adanos, ani Innos, ani Beliar nie mieli zadnej wladzy.\
W miejscu tym lad i chaos wspolistnialy w harmonii – Tak o to powstalo morze.\
A z morza wylonil sie lad, a na ladzie powstalo wszystko to, co zywe…\
Rosliny i zwierzeta, wilki i owce, a na samym koncu powstali ludzie.\
Adanos cieszyl sie, ze wszystkiego, co wowczas powstalo, a swa miloscia darzyl jednakowo wszystkie rzeczy.\
Ale gniew Beliara byl tak wielki, ze przemierzyl on cala Ziemie, by znalezc bestie.\
A gdy do niej przemowil, stala sie ona jego sluga.\
Beliar tchnal w nia czesc swej boskiej mocy, by mogla zniszczyc cala Ziemie.\
Ale Innos podpatrzyl czyn Beliara i przemierzyl Ziemie, by znalezc czlowieka.\
A gdy do niego przemowil, ten stal sie jego sluga.\
Innos tchnal w niego czesc swojej boskiej mocy, by mogl on naprawic szkody wyrzadzone przez Beliara.\
Wtedy zwrocil sie Beliar do innej istoty, ale Adanos zeslal potezna fale, ktora zmyla ja z powierzchni Ziemi.\
Ale wraz z nia odeszly takze drzewa i zwierzeta, wiec Adanos wielce sie zasmucil.\
I rzekl wreszcie do swych braci – Nigdy wiecej nie postanie wasza noga na mojej Ziemi, bo jest ona swieta i pozostanie taka na wieki.\
Ale czlowiek i bestia nie zaprzestali wojny na Ziemi Adanosa i plonal w nich gniew ich bogow.\
A czlowiek pokonal bestie, ktora wrocila do krolestwa Beliara.\
I zobaczyl Adanos, ze prysla rownowaga miedzy ladem a chaosem i zaklal Innosa, by ten odebral czlowiekowi swa boska moc.\
A Innos w swej madrosci tak uczynil. Ale Adanos obawial sie, ze pewnego dnia bestia powroci na Ziemie.\
Dlatego uprosil Innosa, by ten zostawil czesc swojej mocy na Ziemi, aby pewnego dnia przywrocic ja czlowiekowi.\
A Innos w swej madrosci tak uczynil.";

revember_buffer *test_buffer1;
revember_buffer *test_buffer2;
revember_buffer *test_buffer3;

void setUp(void)
{
}

void tearDown(void)
{
}

/* MAX_BUFFER_NUMBER set to value 2 */
void test_revember_buffer_init()
{


    // /* check if it is possible to allocate more than MAX_BUFFER_NUMBER */
    // TEST_ASSERT_EQUAL(BUFFER_OK, buffer_init(&test_buffer1));
    // TEST_ASSERT_NOT_NULL(test_buffer1);
    // TEST_ASSERT_EQUAL(BUFFER_OK, buffer_init(&test_buffer2));
    // TEST_ASSERT_NOT_NULL(test_buffer2);
    // TEST_ASSERT_EQUAL(BUFFER_ERROR, buffer_init(&test_buffer3));
    // TEST_ASSERT_NULL(test_buffer3);

}

/* put value to buffer once and try to get it back */
void test_buffer_put_and_get_01()
{
    // uint8_t test_data[] = "Ale Beliar nie znosil widoku swiatla i niszczyl wszystko";
    // uint8_t out_data[MAX_BUFFER_SIZE];

    // buffer_put(test_buffer1, test_data, sizeof(test_data));
    // uint8_t size = buffer_get_size(test_buffer1);
    // TEST_ASSERT_EQUAL(57, size);
    // buffer_get(test_buffer1, out_data, size);
    // TEST_ASSERT_EQUAL_UINT8_ARRAY(test_data, out_data, size);
    
}

/* put data and receive it in smaller packets */
void test_buffer_put_and_get_02()
{
    // uint8_t test_data[128]; 
    // memcpy(vatras_monolog, test_data, 128);
    // uint8_t out_data[MAX_BUFFER_SIZE];

    // TEST_ASSERT_EQUAL(BUFFER_OK,buffer_put(test_buffer1, test_data, 128));
    // uint8_t size = buffer_get_size(test_buffer1);
    // TEST_ASSERT_EQUAL(128, size);
    // char fail_message[20];
    // for(int i = 0; i < 8; i++)
    // {
    //     TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(test_buffer1, out_data, 16));
    //     sprintf(fail_message, "FAILED AD %d", i);
    //     TEST_ASSERT_EQUAL_UINT8_ARRAY_MESSAGE(test_data + i*16, out_data, 16, fail_message);
    // }
    
}

/* put data and receive it in smaller packets - check if pointer wraps around */
void test_buffer_put_and_get_03()
{
    // uint8_t test_data[512]; 
    // memcpy(vatras_monolog, test_data, 128);
    // uint8_t out_data[MAX_BUFFER_SIZE];
    
    // for(int j = 0; j<4; j++)  
    // {

    //     TEST_ASSERT_EQUAL(BUFFER_OK, buffer_put(test_buffer1, test_data + j*128, 128));
    //     uint8_t size = buffer_get_size(test_buffer1);
    //     TEST_ASSERT_EQUAL(128, size);
    //     char fail_message[20];
    //     for(int i = 0; i < 8; i++)
    //     {
    //         TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(test_buffer1, out_data, 16));
    //         sprintf(fail_message, "FAILED AD %d %d", i, j);
    //         TEST_ASSERT_EQUAL_UINT8_ARRAY_MESSAGE(test_data + i*16+j*128, out_data, 16, fail_message);
    //     }
    // }
}

/* buffer overflow */
void test_buffer_put_and_get_04_overflow()
{
    // uint8_t test_data[256]; 
    // memcpy(vatras_monolog, test_data, 256);
    // uint8_t out_data[MAX_BUFFER_SIZE];

    // TEST_ASSERT_EQUAL(BUFFER_OK, buffer_put(test_buffer1, test_data, 256));
    // /* add 1 more bytes over limit */
    // TEST_ASSERT_EQUAL(BUFFER_BUSY, buffer_put(test_buffer1, test_data+256, 1));

    // uint16_t size = buffer_get_size(test_buffer1);
    // TEST_ASSERT_EQUAL(256, size);
    // char fail_message[20];
    // for(int i = 0; i < 16; i++)
    // {
    //     sprintf(fail_message, "FAILED AD %d", i);
    //     TEST_ASSERT_EQUAL_MESSAGE(BUFFER_OK, buffer_get(test_buffer1, out_data, 16), fail_message);

    //     TEST_ASSERT_EQUAL_UINT8_ARRAY_MESSAGE(test_data + i*16, out_data, 16, fail_message);
    // }
    // TEST_ASSERT_EQUAL(BUFFER_EMPTY, buffer_get(test_buffer1, out_data, 1));
    
}

/* buffer clean */
void test_buffer_put_and_get_05_clean()
{
    // uint8_t test_data[256]; 
    // memcpy(vatras_monolog, test_data, 256);
    // uint8_t out_data[MAX_BUFFER_SIZE];

    // TEST_ASSERT_EQUAL(BUFFER_OK, buffer_put(test_buffer1, test_data, 256));
    
    // buffer_clear(test_buffer1);

    // TEST_ASSERT_EQUAL(0, buffer_get_size(test_buffer1));

    // TEST_ASSERT_EQUAL(BUFFER_EMPTY, buffer_get(test_buffer1, out_data, 1));
    
}

typedef enum
{
	IN_ISR,
	IN_THREAD,
}mcu_mode;

typedef enum
{
	TRANSMIT_INTERFACE_ACTIVE,
	TRANSMIT_INTERFACE_INACTIVE,
}transmit_interface_status_t;

typedef enum
{
	REVEMBER_LOGGER_ACTIVE,
	REVEMBER_LOGGER_NOT_INITIALIZED,
	REVEMBER_LOGGER_SUSPENDED,
}revember_logger_status_t;


extern revember_buffer *data_buffer;
extern revember_buffer *header_buffer;

extern uint16_t last_scenario_id; 
extern uint16_t last_msg_type;
extern uint16_t last_size;

extern volatile revember_logger_status_t revember_logger_status;
extern volatile transmit_interface_status_t transmit_interface_status;
extern uint8_t allocated_buffer_count;
extern mcu_mode revember_check_mcu_mode();

extern uint8_t buffer_array[MAX_BUFFER_NUMBER][MAX_BUFFER_SIZE];
extern revember_buffer my_buffer[MAX_BUFFER_NUMBER];

void test_revember_init()
{
    //allocated_buffer_count = 0;

    TEST_ASSERT_EQUAL(REVEMBER_OK, revember_logger_init(transmit_function));
    TEST_ASSERT_EQUAL(REVEMBER_LOGGER_ACTIVE, revember_logger_status);
    TEST_ASSERT_EQUAL(2, allocated_buffer_count);
    TEST_ASSERT_NOT_NULL(header_buffer);
    TEST_ASSERT_NOT_NULL(data_buffer);


    TEST_ASSERT_EQUAL_PTR(data_buffer, &(my_buffer[0]));
    TEST_ASSERT_EQUAL_PTR(header_buffer, &(my_buffer[1]));

    TEST_ASSERT_EQUAL_PTR(data_buffer->buffer, buffer_array[0]);
    TEST_ASSERT_EQUAL_PTR(header_buffer->buffer, buffer_array[1]);

}

void test_revember_check_mcu_mode()
{
    /* called from ISR */
    __get_IPSR_ExpectAndReturn(1);
    TEST_ASSERT_EQUAL(IN_ISR, revember_check_mcu_mode());
    /* called from THREAD */
    __get_IPSR_ExpectAndReturn(0);
    TEST_ASSERT_EQUAL(IN_THREAD, revember_check_mcu_mode());
}

void test_revEMBer_prepare_header_frame()
{
    uint8_t test_frame[7] = {0x55, 0xBB, 0xAA, 0xDD, 0xCC, 0xEE, 0xFF};
    uint8_t out_frame[7];
    revEMBer_prepare_header_frame(0xAABB, 0xCCDD, 0xFFEE, out_frame);

    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_frame, 7);

}

void test_transmission_possible()
{
    /* transmit interface not active */
    TEST_ASSERT_FALSE(transmission_possible());

    revEMBer_transmit_interface_active();
    /* function called from ISR */
    __get_IPSR_ExpectAndReturn(1);
    TEST_ASSERT_FALSE(transmission_possible());

    /* transmission possible */
    __get_IPSR_ExpectAndReturn(0);
    TEST_ASSERT_TRUE(transmission_possible());
}

void helper_transmit_function(uint16_t size, uint8_t* data)
{

}


void test_revember_buffer_frame()
{
    /* buffer first frame */
    uint8_t test_frame[100];
    TEST_ASSERT_NOT_NULL(header_buffer);
    TEST_ASSERT_NOT_NULL(data_buffer);


    memcpy(test_frame, vatras_monolog, 100);
    revember_buffer_frame(1,2,100, test_frame);
    TEST_ASSERT_EQUAL(100, last_size);
    TEST_ASSERT_EQUAL(2, last_msg_type);
    TEST_ASSERT_EQUAL(1, last_scenario_id);
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(100, buffer_get_size(data_buffer));

    revember_buffer_frame(1,2,50, test_frame);
    TEST_ASSERT_EQUAL(150, last_size);
    TEST_ASSERT_EQUAL(2, last_msg_type);
    TEST_ASSERT_EQUAL(1, last_scenario_id);
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(150, buffer_get_size(data_buffer));

    revember_buffer_frame(1,0,50, test_frame);
    TEST_ASSERT_EQUAL(50, last_size);
    TEST_ASSERT_EQUAL(0, last_msg_type);
    TEST_ASSERT_EQUAL(1, last_scenario_id);
    TEST_ASSERT_EQUAL(7, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(200, buffer_get_size(data_buffer));

    revember_buffer_frame(1,0,50, test_frame);
    TEST_ASSERT_EQUAL(100, last_size);
    TEST_ASSERT_EQUAL(0, last_msg_type);
    TEST_ASSERT_EQUAL(1, last_scenario_id);
    TEST_ASSERT_EQUAL(7, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(250, buffer_get_size(data_buffer));

    revember_finish_buffering();
    TEST_ASSERT_EQUAL(0, last_size);
    TEST_ASSERT_EQUAL(0, last_msg_type);
    TEST_ASSERT_EQUAL(0, last_scenario_id);
    TEST_ASSERT_EQUAL(14, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(250, buffer_get_size(data_buffer));
    
    uint8_t out_buffer[100];
    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(data_buffer, out_buffer, 100));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_buffer, 100);

    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(data_buffer, out_buffer, 50));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_buffer, 50);

    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(data_buffer, out_buffer, 50));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_buffer, 50);

    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(data_buffer, out_buffer, 50));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_buffer, 50);
    TEST_ASSERT_EQUAL(0, buffer_get_size(data_buffer));

    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(header_buffer, out_buffer, 7));
    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(header_buffer, out_buffer, 7));
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));

}


void test_void_revEMBer_transmit_bytes()
{
    uint8_t data[8];
    transmit_function_Expect(data, 8);
    revEMBer_transmit_bytes(data, 8);
}

uint16_t offset = 0;
uint8_t captured_data[MAX_BUFFER_SIZE];

void capture_message(uint8_t *data, uint16_t size)
{
    memcpy(captured_data+offset, data, size);
    offset += size;
}

void test_revember_send_frame()
{
    /* transission possible */

    /*configure mocks*/
    transmit_function_AddCallback(capture_message);
    __get_IPSR_ExpectAndReturn(0);
    transmit_function_Expect(NULL, 7);
    transmit_function_IgnoreArg_data();
    transmit_function_Expect(NULL, 100);
    transmit_function_IgnoreArg_data();

    uint8_t test_frame[100];
    uint8_t test_header[7];
    revEMBer_prepare_header_frame(0,1,100, test_header);

    memcpy(test_frame, vatras_monolog, 100);
    revember_send_frame(0, 1, 100, test_frame);
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_header, captured_data, 7);
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, captured_data+7, 100);

    /* transmission impossible - called from ISR */
    __get_IPSR_ExpectAndReturn(1);
    //revEMBer_transmit_interface_inactive();
    revEMBer_prepare_header_frame(29,1,100, test_header);

    memcpy(test_frame, vatras_monolog, 100);
    revember_send_frame(29, 1, 100, test_frame);
    uint8_t out_buffer[100];
    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(data_buffer, out_buffer, 100));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_buffer, 100);
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));

    revember_finish_buffering();
    TEST_ASSERT_EQUAL(7, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(header_buffer, out_buffer, 7));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_header, out_buffer, 7);
    
}

void test_revember_WSEQ_transsmittion_possible()
{
    offset = 0;

    uint8_t test_frame[100] = {0x1, 0xBB, 0xAA, 0x00, 0x00,
                               0x2, 0xDD, 0xCC, 0x00, 0x00,
                               0x3, 0xFF, 0xFF, 0x00, 0x00, 
                               0x4, 0x11, 0x99, 0x00, 0x00,
                            };
    uint8_t test_header[7];

    transmit_function_AddCallback(capture_message);
    __get_IPSR_ExpectAndReturn(0);
    transmit_function_Expect(NULL, 7);
    transmit_function_IgnoreArg_data();
    transmit_function_Expect(NULL, 20);
    transmit_function_IgnoreArg_data();
    revEMBer_WSEQ(4, 0, 1, 0xAABB, 2, 0xCCDD, 3, 0xFFFF, 4, 0x9911);
    
    revEMBer_prepare_header_frame(0, 1, 20, test_header);
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_header, captured_data, 7);
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, captured_data+7, 20);

    /* no data shall be buffered */
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(0, buffer_get_size(data_buffer));

}

void test_revember_WSEQ_transsmittion_not_possible()
{
    offset = 0;

    uint8_t test_frame[100] = {0x1, 0xBB, 0xAA, 0x00, 0x00,
                               0x2, 0xDD, 0xCC, 0x00, 0x00,
                               0x3, 0xFF, 0xFF, 0x00, 0x00, 
                               0x4, 0x11, 0x99, 0x00, 0x00,
                               0x1, 0x00, 0x80, 0x00, 0x00,
                               0x2, 0x33, 0x11, 0x00, 0x00,
                            };
    uint8_t test_header[7];

    __get_IPSR_ExpectAndReturn(1);
    __get_IPSR_ExpectAndReturn(1);
    __get_IPSR_ExpectAndReturn(1);
    revEMBer_WSEQ(4, 0, 1, 0xAABB, 2, 0xCCDD, 3, 0xFFFF, 4, 0x9911);
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(20, buffer_get_size(data_buffer));
    revEMBer_WSEQ(2, 0, 1, 0x8000, 2, 0x1133);
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(30, buffer_get_size(data_buffer));
    revEMBer_WSEQ(4, 2, 1, 0xAABB, 2, 0xCCDD, 3, 0xFFFF, 4, 0x9911);
    TEST_ASSERT_EQUAL(7, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(50, buffer_get_size(data_buffer));
    revember_finish_buffering();
    TEST_ASSERT_EQUAL(14, buffer_get_size(header_buffer));
    
    revEMBer_prepare_header_frame(0, 1, 30, test_header);
    uint8_t out_buffer[MAX_BUFFER_SIZE];
    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(header_buffer, out_buffer, 7));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_header, out_buffer, 7);

    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(data_buffer, out_buffer, 30));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_buffer, 20);

    revEMBer_prepare_header_frame(2, 1, 20, test_header);
    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(header_buffer, out_buffer, 7));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_header, out_buffer, 7);
    TEST_ASSERT_EQUAL(BUFFER_OK, buffer_get(data_buffer, out_buffer, 20));
    TEST_ASSERT_EQUAL_UINT8_ARRAY(test_frame, out_buffer, 20);
    
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(0, buffer_get_size(data_buffer));
}

void test_revember_buffer_flush_test()
{
    offset = 0;

    uint8_t test_frame[100] = {0x1, 0xBB, 0xAA, 0x00, 0x00,
                               0x2, 0xDD, 0xCC, 0x00, 0x00,
                               0x3, 0xFF, 0xFF, 0x00, 0x00, 
                               0x4, 0x11, 0x99, 0x00, 0x00,
                               0x1, 0x00, 0x80, 0x00, 0x00,
                               0x2, 0x33, 0x11, 0x00, 0x00,
                            };
    uint8_t test_header[7];

    __get_IPSR_ExpectAndReturn(1);
    __get_IPSR_ExpectAndReturn(1);
    __get_IPSR_ExpectAndReturn(1);
    revEMBer_WSEQ(4, 0, 1, 0xAABB, 2, 0xCCDD, 3, 0xFFFF, 4, 0x9911);
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(20, buffer_get_size(data_buffer));
    revEMBer_WSEQ(2, 0, 1, 0x8000, 2, 0x1133);
    TEST_ASSERT_EQUAL(0, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(30, buffer_get_size(data_buffer));
    revEMBer_WSEQ(4, 2, 1, 0xAABB, 2, 0xCCDD, 3, 0xFFFF, 4, 0x9911);
    TEST_ASSERT_EQUAL(7, buffer_get_size(header_buffer));
    TEST_ASSERT_EQUAL(50, buffer_get_size(data_buffer));
    
    transmit_function_Expect(NULL, 7);
    transmit_function_IgnoreArg_data();
    transmit_function_Expect(NULL, 30);
    transmit_function_IgnoreArg_data();
    transmit_function_Expect(NULL, 7);
    transmit_function_IgnoreArg_data();
    transmit_function_Expect(NULL, 20);
    transmit_function_IgnoreArg_data();

    transimt_buffer_flush();


    
}

#endif // TEST
