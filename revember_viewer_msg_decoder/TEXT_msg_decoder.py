
class TEXT_Decoder:

    def __init__(self, callback = None):
        self.callback = callback

    def attach_user_callbacks(self, callback):
        self.user_callback = callback

    def data_processing(self, datasize: int, data : bytes, display_options):
        ret_val = "|"+"-"*display_options.get_current_indent() +  f'text msg: {str(data, 'UTF-8')}' + "\n"
        if self.callback != None:
            self.callback(data)
        return ret_val


class Text_Callback_Processing:

    def __init__(self):
        self.my_files = set()
        self.active = False
        print("TEXT_ADDED")

    def text_processing(self, data):
        text = str(data, 'UTF-8')


        if text == "START":
            print("started")
            self.active = True
        elif text == "STOP":
            print("stopped")
            self.active = False
            for f in self.my_files:
                print(f)
        else:
            if self.active:
                self.my_files.add(text)