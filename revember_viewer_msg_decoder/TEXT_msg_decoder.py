
class TEXT_Decoder:

    def data_processing(self, datasize: int, data : bytes, display_options):
        ret_val = "|"+"-"*display_options.get_current_indent() +  f'text msg: {str(data, 'UTF-8')}' + "\n"
        return ret_val

