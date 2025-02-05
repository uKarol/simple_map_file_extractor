from param_decoder import *

class GlobalDecoder:

    def __init__(self, user_defined_params = None):
        self.predefined_params = [0]
        self.useuser_defined_params = None
        self.user_defined_callbacks = None

        self.predefined_dict = { 0 : self.decode_text,
                                 1 : self.link_reg_decode,
                                 2 : self.map_pointer_decode,
                                }
    
    def link_reg_decode(self, packet_info:Packet, packet_data):
        pass

    def map_pointer_decode(self, packet_info:Packet, packet_data):
        pass

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
            ret_val = self.default_handler()
        return ret_val
    