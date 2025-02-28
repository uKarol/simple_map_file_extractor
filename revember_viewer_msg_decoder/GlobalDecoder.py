from revember_viewer_msg_decoder.param_decoder import *

class MapDetailsGetter:

    def __init__(self, decode_address, decode_LR_PC):
        self.decode_address = decode_address
        self.decode_LR_PC = decode_LR_PC

    def decode_addr(self, address):
        ret_val = self.decode_address(address)
        if(ret_val != None):
            ret_val = ret_val[0]
        return ret_val
    
    def decode_LRPC(self, address):
        ret_val = self.decode_LR_PC(address)
        if(ret_val != None):
            ret_val = ret_val[0]
            #print(ret_val[0])
        else:
            print(hex(address))
        return ret_val
    
class PredefinedHandler:

    def __init__(self, map_getter): 
        self.map_getter = map_getter
        self.indent = 0

    def FUNCTION_ENTRY_handler(self, packet_data):
        ret_val = "|"+"-"*self.indent + f'{self.map_getter.decode_LRPC(packet_data)} entry \n'
        #self.indent = self.indent+1
        return ret_val
    
    def FUNCTION_EXIT_handler(self, packet_data):
        #self.indent = self.indent-1
        ret_val = "|"+"-"*self.indent +  f'{self.map_getter.decode_LRPC(packet_data)} exit \n'
        return ret_val

    def FUNCTION_RETURN_handler(self, packet_data):
        return f"ret_val: {packet_data} \n"

    def LINK_REGISTER_handler(self, packet_data):
        ret_val = "|"+"-"*self.indent +  f'called by: {self.map_getter.decode_LR_PC(packet_data)[0]} \n'
        return ret_val
	
    def FUNCTION_POINTER_handler(self, packet_data):
        print(packet_data)
        ret_val = f'function by pointer: {self.map_getter.decode_addr(packet_data-1) }\n'
        return ret_val
	
    def VARIABLE_POINTER_handler(self, packet_data):
        ret_val = f'variable by pointer: {self.map_getter.decode_addr(packet_data) }\n'
        return ret_val

    def reset_indentation(self):
        self.indent = 0

class GlobalHandler:

    def __init__(self, map_getter):
        self.predefined_handler = PredefinedHandler(map_getter)
        self.predefined_methods = self.get_predefined_methods(PredefinedHandler)

    def reset_indentation(self):
        self.predefined_handler.reset_indentation()

    def get_predefined_methods(self, handler_class):
        found_methods = [meth for meth in handler_class.__dict__ if callable( getattr(handler_class, meth) )and not meth.startswith('__') ]
        return found_methods

    def default_handler(self, packet_info:Packet, packet_data):
        ret_val = f'cannot decode \nparam id: {packet_info} \nraw data {packet_data} \n'
        return ret_val

    def decode(self, packet_info:Packet, packet_data):
        try:
            method_name = self.predefined_methods[packet_info]
            ret_val : str
            #if method_name in self.predefined_methods:
            handler = getattr(PredefinedHandler, method_name)
            ret_val = handler(self.predefined_handler, packet_data)
            #else: 
        except IndexError as ex:
            ret_val = self.default_handler(packet_info, packet_data)
        return ret_val

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

class WordSequence_protocol_decoder:

    def __init__(self, map_getter):
        self.decoder = GlobalHandler(map_getter)

    def reset_indentation(self):
       self.decoder.reset_indentation()

    def packet_processing(self, info : Packet, packet : bytes):
        number_of_params = info.datasize//5
        WordSequence_frame = WordSequence_Frame()
        WordSequence_frame.set_length(number_of_params)
        WordSequence_frame.unpack(packet)
        if(number_of_params == 1):
            return self.decoder.decode(WordSequence_frame.x.id, WordSequence_frame.x.value)
        else:
            ret_val = ""
            for i in range(0, number_of_params):
                ret_val += self.decoder.decode(WordSequence_frame.x[i].id, WordSequence_frame.x[i].value)
            return ret_val