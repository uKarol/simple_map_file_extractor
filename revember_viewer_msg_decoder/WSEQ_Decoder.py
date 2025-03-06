from revember_viewer_msg_decoder.HeaderDecoder import *
from revember_viewer_msg_decoder.WSEQ_Handler import *
from revember_viewer_msg_decoder.WSEQ_HelperFunctions import *
    
import cstruct

class WordSequence_Unit(cstruct.MemCStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __def__ = """
        struct {
            uint8_t id;
            uint32_t value;
        }
    """

class WordSequence_Frame(cstruct.MemCStruct):
    __byte_order__ = cstruct.BIG_ENDIAN
    __def__ = """

    typedef struct WordSequence_Unit WordSequence_Unit;
    
        struct {
            WordSequence_Unit x[];
        }
    """

    def set_length(self, length):
        self.set_flexible_array_length(length)


class WordSequenceProtocolDecoder:

    def __init__(self, map_getter):
        self.protocol_handler = WordSequenceHandler(map_getter)
        self.predefined_methods = self._get_predefined_methods(WordSequenceHandler)

    def _get_predefined_methods(self, handler_class):
        found_methods = [meth for meth in handler_class.__dict__ if callable( getattr(handler_class, meth) )and not meth.startswith('__') ]
        return found_methods
    
    def _default_WSEQ_handler(self, param_id: int, packet_data):
        ret_val = f'cannot decode \nparam id: {param_id} \nraw data {hex(packet_data)} \n'
        return ret_val

    def _run_handler(self, param_id: int, packet_data, indent):
        try:
            method_name = self.predefined_methods[param_id]
            ret_val : str
            handler = getattr(WordSequenceHandler, method_name)
            ret_val = handler(self.protocol_handler, packet_data, indent)
        except IndexError as ex:
            ret_val = self._default_WSEQ_handler(param_id, packet_data)
        return ret_val

    def data_processing(self, datasize: int, data : bytes, indent):
        number_of_params = datasize//5
        WordSequence_frame = WordSequence_Frame()
        WordSequence_frame.set_length(number_of_params)
        WordSequence_frame.unpack(data)
        if(number_of_params == 1):
            return self._run_handler(WordSequence_frame.x.id, WordSequence_frame.x.value, indent)
        else:
            ret_val = ""
            for i in range(0, number_of_params):
                ret_val += self._run_handler(WordSequence_frame.x[i].id, WordSequence_frame.x[i].value, indent)
            return ret_val
        


