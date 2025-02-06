from param_decoder import *

class MapDetailsGetter:

    def __init__(self, decode_address, decode_LR_PC):
        self.decode_address = decode_address
        self.decode_LR_PC = decode_LR_PC

    def decode_address(self, address):
        return self.decode_address(address)

    def decode_LR_PC(self, address):
        return self.decode_LR_PC(address)


class GlobalDecoder:

    def __init__(self, map_getter):
        self.predefined_params = [0, 1, 2]
        self.useuser_defined_params = None
        self.user_defined_callbacks = None
        self.map_getter = map_getter
        self.predefined_dict = { 0 : self.decode_text,
                                 1 : self.link_reg_decode,
                                 2 : self.map_pointer_decode,
                                }
    
    def link_reg_decode(self, packet_info:Packet, packet_data):
        reg_value = int.from_bytes(packet_data)
        ret_val = f'function called by {self.map_getter.decode_LR_PC(reg_value)}'
        return ret_val

    def map_pointer_decode(self, packet_info:Packet, packet_data):
        ptr_value = int.from_bytes(packet_data, byteorder='little')
        #print(f'ptr_value {hex(ptr_value)}')
        ret_val = f'object name: {self.map_getter.decode_address(ptr_value-1) }\n'
        return ret_val

    def decode_text(self, packet_info:Packet, packet_data):
        ret_val = str(packet_data, 'UTF-8') + '\n'
        return ret_val

    def default_handler(self, packet_info:Packet, packet_data):
        ret_val = f'cannot decode \nparam id: {packet_info.param} \nraw data {packet_data} \n'
        return ret_val

    def predefined_param_handler(self, packet_info:Packet, packet_data):
        handler = self.predefined_dict[packet_info.param]
        return handler(packet_info, packet_data)


    def decoder(self, packet_info:Packet, packet_data):
        ret_val : str
        if packet_info.param in self.predefined_params:
            ret_val = self.predefined_param_handler(packet_info, packet_data)
        else: 
            ret_val = self.default_handler(packet_info, packet_data)
        return ret_val
    