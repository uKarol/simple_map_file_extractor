class WordSequenceHandler:

    def __init__(self, helper_functions): 
        self.helper_functions = helper_functions

    def FUNCTION_ENTRY_handler(self, packet_data, display_options):
        ret_val = "|"+"-"*display_options.indent + f'{self.helper_functions.decode_LR_or_PC(packet_data)} entry \n'
        display_options.indent = display_options.indent + 1
        return ret_val
    
    def FUNCTION_EXIT_handler(self, packet_data, display_options):
        display_options.indent = display_options.indent-1
        ret_val = "|"+"-"*display_options.indent +  f'{self.helper_functions.decode_LR_or_PC(packet_data)} exit \n'
        return ret_val

    def FUNCTION_RETURN_handler(self, packet_data, display_options):
        return "|"+"-"*display_options.indent + f"ret_val: {packet_data} \n"

    def LINK_REGISTER_handler(self, packet_data, display_options):
        ret_val = "|"+"-"*display_options.indent +  f'called by: {self.helper_functions.decode_LR_or_PC(packet_data)} \n'
        return ret_val
	
    def FUNCTION_POINTER_handler(self, packet_data, display_options):
        print(packet_data)
        ret_val = f'function by pointer: {self.helper_functions.decode_addr(packet_data-1) }\n'
        return ret_val
	
    def VARIABLE_POINTER_handler(self, packet_data, display_options):
        ret_val = f'variable by pointer: {self.helper_functions.decode_addr(packet_data) }\n'
        return ret_val
