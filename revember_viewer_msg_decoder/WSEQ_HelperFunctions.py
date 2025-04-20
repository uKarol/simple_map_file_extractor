from dataclasses import dataclass

@dataclass
class map_object:
    name: str
    section: str
    location: str
    address: int


class DecoderHelperFunctions:

    def __init__(self, decode_address, decode_LR_PC):
        self.decode_address = decode_address
        self.decode_LR_PC = decode_LR_PC

    def empty_return(self, address):
        return map_object(f"Not found {hex(address)}", "Not found", "Not found", address)

    def decode_addr(self, address: int):
        temp = self.decode_address(address)
        if(temp != None):
            ret_val = map_object(*temp)  
        else:
            ret_val = self.empty_return(address)  
        return ret_val
        
    def decode_LR_or_PC(self, address: int):
        temp = self.decode_LR_PC(address)
        if(temp != None):
            ret_val = map_object(*temp)
        else:
            ret_val = self.empty_return(address)
        return ret_val