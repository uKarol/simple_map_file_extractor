import sys
import os
# setting path
sys.path.append('..')

from revember_viewer_msg_decoder.HeaderDecoder import *
from revember_viewer_msg_decoder.WSEQ_Decoder import *
from revember_viewer_msg_decoder.GlobalDecoder import *


print("testing")

def decode_address(address):
    ret =  ["DECODE ADDRESS",0]
    return ret
        
def decode_LR_or_PC(address):
    ret = ["DECODE LR/PC", 0]  
    return ret
    
mgetter = MapDetailsGetter(decode_address, decode_LR_or_PC)

dec = GenericDataDecoder(mgetter)

hf = HeaderFrame(scenario = 0, id = 0, datasize = 20)
arg = bytes.fromhex("0080808080038080808002112233440112341234")

print(dec.decode(hf, arg))

# if __name__ == "__main__":

#     class tester:
        
#         def __init__(self):
#             self.indent = [0]
#             hf = DecoderHelperFunctions(self.decode_address, self.decode_LR_or_PC)
#             test_prot = WordSequenceProtocolDecoder(hf)
#             print(test_prot.predefined_methods)
#             arg = bytes.fromhex("0080808080038080808002112233440112341234")
#             print(test_prot._run_handler(0, 1111, self.indent))
#             print(test_prot._run_handler(3, 1111, self.indent))
#             print(test_prot._run_handler(2, 1111, self.indent))
#             print(test_prot._run_handler(1, 1111, self.indent))

#             print(test_prot.data_processing(20, arg, self.indent))
    
#         def decode_address(self, address):
#             ret =  ["DECODE ADDRESS",0]
#             return ret
        
#         def decode_LR_or_PC(self, address):
#             ret = ["DECODE LR/PC", 0]  
#             return ret
        
#     tester()