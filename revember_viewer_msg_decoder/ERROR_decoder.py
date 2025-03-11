class ERROR_Decoder:

    error_description = {
        0: "DATA BUFFER OVERFLOW",
    }

    def data_processing(self, datasize: int, data : bytes, display_options):
        err_code = int.from_bytes(data, "big")
        try: 
            ret_val = "|"+"-"*display_options.indent +  f'ERROR DURING LOGGING OCCURED: {self.error_description[err_code]} \n'
        except KeyError as ex:
            ret_val = "|"+"-"*display_options.indent +  f'UNEXPECTED ERROR DURING LOGGING OCCURED: {err_code} \n'
        
        return ret_val