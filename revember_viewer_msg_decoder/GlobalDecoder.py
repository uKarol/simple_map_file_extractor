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
        self.indentation_active = True
        for i in range (0, scenarios_nuber):
            self.scn.append(RevemberScenario(0)) 
        self.last_used_scenario = 0

    def enable_default_indent(self):
        self.indentation_active = True

    def disable_default_indent(self):
        self.indentation_active = False

    def increase_indent(self):
        if self.indentation_active:
            self.scn[self.last_used_scenario].indent = self.scn[self.last_used_scenario].indent + 1

    def decrease_indent(self):
        if self.indentation_active and self.scn[self.last_used_scenario].indent > 0:
            self.scn[self.last_used_scenario].indent = self.scn[self.last_used_scenario].indent - 1

    def get_current_indent(self):
        return self.scn[self.last_used_scenario].indent 

    def get_scn(self, num):
        return self.scn[num]

    def reset_indent(self, num):
        self.scn[num].indent = 0

    def set_scenario(self, scenario):
        addition = ""
        if(self.last_used_scenario != scenario):
            addition = f"SCENARIO CHANGED {scenario}\n"
        self.last_used_scenario = scenario
        return addition

class GenericDataDecoder:

    def __init__(self, map_getter):
        self.handlers = {   0: TEXT_Decoder(),
                            1: WordSequenceProtocolDecoder(map_getter),
                            2: ERROR_Decoder(),
                         }
        self.scn_number = 256
        self.scn_mgr = RevemberScenarioManager(self.scn_number)

    def enable_default_indent(self):
        self.scn_mgr.enable_default_indent()

    def disable_default_indent(self):
        self.scn_mgr.disable_default_indent()
        self.reset_indentation()

    def reset_indentation(self):
        for i in range(1,self.scn_number):
            self.scn_mgr.reset_indent(i)

    def default_handler(self, header:HeaderFrame, packet_data):
        ret_val = f'cannot decode \nparam id: {header.id} \nraw data {packet_data} \n'
        return ret_val

    def decode(self, header:HeaderFrame, packet_data):
        ret_val = ""
        try:
            addition = self.scn_mgr.set_scenario(header.scenario)
            ret_val = addition + self.handlers[header.id].data_processing(header.datasize, packet_data, self.scn_mgr)
        except IndexError as ex:
            ret_val = self.default_handler(header, packet_data)
        except KeyError as ex:
            ret_val = self.default_handler(header, packet_data)
        return ret_val

