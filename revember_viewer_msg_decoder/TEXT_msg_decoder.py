
class TEXT_Decoder:

    def data_processing(self, datasize: int, data : bytes, display_options):
        ret_val = "|"+"-"*display_options.indent +  f'text msg: {str(data, 'UTF-8')} \n'
        #ret_val = str(data, 'UTF-8')
        return ret_val

