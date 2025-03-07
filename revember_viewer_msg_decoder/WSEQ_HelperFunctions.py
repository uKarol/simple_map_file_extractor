    
class DecoderHelperFunctions:

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
            ret_val = f'address hex(address) not found'
        return ret_val