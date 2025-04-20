class WordSequenceHandler:

    def __init__(self, helper_functions, user_handlers): 
        self.helper_functions = helper_functions
        self.user_handler = user_handlers

    def FUNCTION_ENTRY_handler(self, packet_data, display_options):
        decoded_data = self.helper_functions.decode_LR_or_PC(packet_data)
        ret_val = "|"+"-"*display_options.get_current_indent() + f'{decoded_data.name} entry \n'
        display_options.increase_indent()
        self.user_handler.wseq_processing(decoded_data, "FUNCTION_ENTRY")
        return ret_val
    
    def FUNCTION_EXIT_handler(self, packet_data, display_options):
        display_options.decrease_indent()
        decoded_data = self.helper_functions.decode_LR_or_PC(packet_data)
        ret_val = "|"+"-"*display_options.get_current_indent() +  f'{decoded_data.name} exit \n'
        self.user_handler.wseq_processing(decoded_data, "FUNCTION_EXIT")
        return ret_val

    def FUNCTION_RETURN_handler(self, packet_data, display_options):
        self.user_handler.wseq_processing(packet_data, "FUNCTION_RET_VAL")
        return "|"+"-"*display_options.get_current_indent() + f"ret_val: {packet_data} \n"
        

    def LINK_REGISTER_handler(self, packet_data, display_options):
        decoded_data = self.helper_functions.decode_LR_or_PC(packet_data)
        ret_val = "|"+"-"*display_options.get_current_indent() +  f'called by: {decoded_data.name} \n'
        self.user_handler.wseq_processing(decoded_data, "LINK_REGISTER")
        return ret_val
	
    def FUNCTION_POINTER_handler(self, packet_data, display_options):
        decoded_data = self.helper_functions.decode_addr(packet_data-1)
        ret_val = f'function by pointer: {decoded_data.name}\n'
        self.user_handler.wseq_processing(decoded_data, "FUNCTION_POINTER")
        return ret_val
	
    def VARIABLE_POINTER_handler(self, packet_data, display_options):
        decoded_data = self.helper_functions.decode_addr(packet_data)
        ret_val = f'variable by pointer: {decoded_data.name}\n'
        self.user_handler.wseq_processing(decoded_data, "VARIABLE_POINTER")
        return ret_val

    def RAW_VALUE_handler(self, packet_data, display_options):
        ret_val = f'raw value: {packet_data}\n'
        self.user_handler.wseq_processing(packet_data, "RAW_VALUE")
        return ret_val