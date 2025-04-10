class WordSequenceHandler:

    def __init__(self, helper_functions, user_handlers): 
        self.helper_functions = helper_functions
        self.user_handler = user_handlers

    def FUNCTION_ENTRY_handler(self, packet_data, display_options):
        ret_val = "|"+"-"*display_options.get_current_indent() + f'{self.helper_functions.decode_LR_or_PC(packet_data)} entry \n'
        display_options.increase_indent()
        return ret_val
    
    def FUNCTION_EXIT_handler(self, packet_data, display_options):
        display_options.decrease_indent()
        ret_val = "|"+"-"*display_options.get_current_indent() +  f'{self.helper_functions.decode_LR_or_PC(packet_data)} exit \n'
        return ret_val

    def FUNCTION_RETURN_handler(self, packet_data, display_options):
        return "|"+"-"*display_options.get_current_indent() + f"ret_val: {packet_data} \n"

    def LINK_REGISTER_handler(self, packet_data, display_options):
        ret_val = "|"+"-"*display_options.get_current_indent() +  f'called by: {self.helper_functions.decode_LR_or_PC(packet_data)} \n'
        return ret_val
	
    def FUNCTION_POINTER_handler(self, packet_data, display_options):
        ret_val = f'function by pointer: {self.helper_functions.decode_addr(packet_data-1) }\n'
        return ret_val
	
    def VARIABLE_POINTER_handler(self, packet_data, display_options):
        ret_val = f'variable by pointer: {self.helper_functions.decode_addr(packet_data) }\n'
        return ret_val

    def RAW_VALUE_handler(self, packet_data, display_options):
        ret_val = f'raw value: {packet_data}\n'
        return ret_val