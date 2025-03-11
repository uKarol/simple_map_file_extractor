
class TEXT_Decoder:

    def data_processing(self, datasize: int, data : bytes, indent):
        ret_val = "|"+"-"*indent[0] +  f'text msg: {str(data, 'UTF-8')} \n'
        #ret_val = str(data, 'UTF-8')
        return ret_val

