from abc import ABC

class Revember_User_Callback(ABC):

    def text_processing(self, data):
        pass

    def wseq_processing(self, data, data_type):
        pass


class User_Callback_Processing(Revember_User_Callback):

    def __init__(self):
        self.my_files = set()
        self.global_stucts = set()
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
            print("possible location of config global variables:")
            for f in self.global_stucts:
                print(f)
        else:
            if self.active:
                self.my_files.add(text)

    def wseq_processing(self, data, data_type):
        
        if self.active:

            if data_type == "VARIABLE_POINTER":
                self.global_stucts.add(data.location)
        