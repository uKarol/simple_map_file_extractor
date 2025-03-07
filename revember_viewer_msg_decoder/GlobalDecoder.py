from revember_viewer_msg_decoder.HeaderDecoder import *
from revember_viewer_msg_decoder.WSEQ_Decoder import *


class MapDetailsGetter:

    def __init__(self, decode_address, decode_LR_PC):
        self.decode_address = decode_address
        self.decode_LR_PC = decode_LR_PC

    def decode_addr(self, address):
        ret_val = self.decode_address(address)
        if(ret_val != None):
            ret_val = ret_val[0]
        return ret_val
    
    def decode_LR_or_PC(self, address):
        ret_val = self.decode_LR_PC(address)
        if(ret_val != None):
            ret_val = ret_val[0]
        else:
            print(hex(address))
        return ret_val
    

class GenericDataDecoder:

    def __init__(self, map_getter):
        self.handlers = {1: WordSequenceProtocolDecoder(map_getter)}
        self.indent = [0]

    def reset_indentation(self):
        self.indent = [0]

    def default_handler(self, header:HeaderFrame, packet_data):
        ret_val = f'cannot decode \nparam id: {header.id} \nraw data {packet_data} \n'
        return ret_val

    def decode(self, header:HeaderFrame, packet_data):
        ret_val = ""
        try:
            ret_val = self.handlers[header.id].data_processing(header.datasize, packet_data, self.indent)
        except IndexError as ex:
            ret_val = self.default_handler(header, packet_data)
        except KeyError as ex:
            rev_val = "INVALID PROTOCOL ID"
        return ret_val

