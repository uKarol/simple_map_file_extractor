class WordSequenceHandler:

    def __init__(self, helper_functions): 
        self.helper_functions = helper_functions

    def FUNCTION_ENTRY_handler(self, packet_data, indent):
        ret_val = "|"+"-"*indent[0] + f'{self.helper_functions.decode_LR_or_PC(packet_data)} entry \n'
        indent[0] = indent[0] + 1
        return ret_val
    
    def FUNCTION_EXIT_handler(self, packet_data, indent):
        indent[0] = indent[0]-1
        ret_val = "|"+"-"*indent[0] +  f'{self.helper_functions.decode_LR_or_PC(packet_data)} exit \n'
        return ret_val

    def FUNCTION_RETURN_handler(self, packet_data, indent):
        return "|"+"-"*indent[0] + f"ret_val: {packet_data} \n"

    def LINK_REGISTER_handler(self, packet_data, indent):
        ret_val = "|"+"-"*indent[0] +  f'called by: {self.helper_functions.decode_LR_or_PC(packet_data)} \n'
        return ret_val
	
    def FUNCTION_POINTER_handler(self, packet_data, indent):
        print(packet_data)
        ret_val = f'function by pointer: {self.helper_functions.decode_addr(packet_data-1) }\n'
        return ret_val
	
    def VARIABLE_POINTER_handler(self, packet_data, indent):
        ret_val = f'variable by pointer: {self.helper_functions.decode_addr(packet_data) }\n'
        return ret_val
