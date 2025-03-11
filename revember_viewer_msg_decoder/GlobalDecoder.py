from revember_viewer_msg_decoder.HeaderDecoder import *
from revember_viewer_msg_decoder.WSEQ_Decoder import *
from revember_viewer_msg_decoder.TEXT_msg_decoder import *
from revember_viewer_msg_decoder.ERROR_decoder import *
from dataclasses import dataclass

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

@dataclass
class RevemberScenario:
    indent : int
class RevemberScenarioManager:

    def __init__(self, scenarios_nuber):
        self.scn = []
        for i in range (0, scenarios_nuber):
            self.scn.append(RevemberScenario(0)) 
        self.last_used_scenario = 0

    def get_scn(self, num):
        return self.scn[num]

    def reset_indent(self, num):
        self.scn[num].indent = 0

class GenericDataDecoder:

    def __init__(self, map_getter):
        self.handlers = {   0: TEXT_Decoder(),
                            1: WordSequenceProtocolDecoder(map_getter),
                            2: ERROR_Decoder(),
                         }
        self.scn_mgr = RevemberScenarioManager(256)

    def reset_indentation(self):
        pass

    def default_handler(self, header:HeaderFrame, packet_data):
        ret_val = f'cannot decode \nparam id: {header.id} \nraw data {packet_data} \n'
        return ret_val

    def decode(self, header:HeaderFrame, packet_data):
        ret_val = ""
        try:
            addition = ""
            if(self.scn_mgr.last_used_scenario != header.scenario):
                addition = f"SCENARIO CHANGED {header.scenario}\n"
            self.scn_mgr.last_used_scenario = header.scenario 
            print(f"scn 0 {self.scn_mgr.scn[0].indent} scn 15 {self.scn_mgr.scn[15].indent} ")   
            ret_val = addition + self.handlers[header.id].data_processing(header.datasize, packet_data, self.scn_mgr.scn[header.scenario])
        except IndexError as ex:
            ret_val = self.default_handler(header, packet_data)
        return ret_val

