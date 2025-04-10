
class TEXT_Decoder:

    def __init__(self, callback = None):
        self.callback = callback.text_processing

    def attach_user_callbacks(self, callback):
        self.user_callback = callback

    def data_processing(self, datasize: int, data : bytes, display_options):
        ret_val = "|"+"-"*display_options.get_current_indent() +  f'text msg: {str(data, 'UTF-8')}' + "\n"
        if self.callback != None:
            self.callback(data)
        return ret_val
