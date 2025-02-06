from param_decoder import *

class MapDetailsGetter:

    def __init__(self, decode_address, decode_LR_PC):
        print("CREATED GETTER")
        self.decode_address = decode_address
        self.decode_LR_PC = decode_LR_PC

    def decode_addr(self, address):
        ret_val = self.decode_address(address)
        if(ret_val != None):
            ret_val = ret_val[0]
        return ret_val
    
    def decode_LR_PC(self, address):
        ret_val = self.decode_LR_PC(address)
        if(ret_val != None):
            ret_val = ret_val[0]
        return ret_val
    
class PredefinedHandler:

    def __init__(self, map_getter):
        self.map_getter = map_getter

    def param_0_handler(self, packet_info:Packet, packet_data):
        ret_val = str(packet_data, 'UTF-8') + '\n'
        return ret_val

    def param_1_handler(self, packet_info:Packet, packet_data):
        reg_value = int.from_bytes(packet_data)
        ret_val = f'function called by {self.map_getter.decode_LR_PC(reg_value)}'
        return ret_val

    def param_2_handler(self, packet_info:Packet, packet_data):
        ptr_value = int.from_bytes(packet_data, byteorder='little')
        ret_val = f'object name: {self.map_getter.decode_addr(ptr_value-1) }\n'
        return ret_val


class GlobalHandler:

    def __init__(self, map_getter):
        self.predefined_handler = PredefinedHandler(map_getter)
        self.predefined_methods = self.get_predefined_methods(PredefinedHandler)

    def get_predefined_methods(self, handler_class):
        found_methods = [meth for meth in handler_class.__dict__ if callable( getattr(handler_class, meth) )]
        return found_methods

    def default_handler(self, packet_info:Packet, packet_data):
        ret_val = f'cannot decode \nparam id: {packet_info.param} \nraw data {packet_data} \n'
        return ret_val

    def decoder(self, packet_info:Packet, packet_data):
        method_name = f'param_{packet_info.param}_handler'
        ret_val : str
        if method_name in self.predefined_methods:
            handler = getattr(PredefinedHandler, method_name)
            ret_val = handler(self.predefined_handler, packet_info, packet_data)
        else: 
            ret_val = self.default_handler(packet_info, packet_data)
        return ret_val
