from map_file_extractor import map_extractor
from DTO_test import *
#from threading import Thread
import time

class MapExtractorController:

    def __init__(self, model, view):
        self.model = model
        #self.thread_active = True
        self.view = view
        self.view.setup(self)
        self.hex_extractor_dto = []
        #self.periodic_thread = Thread(target=self.periodic_refresh, daemon=True) 

    def periodic_refresh(self):
        while(self.thread_active):
            time.sleep(2)
            t = time.localtime()
            current_time = time.strftime(" %H:%M:%S", t)
            self.view.show_info_object(current_time + '\n')

    def find_object_by_name(self):
        name = self.view.get_object_name()
        info = self.model.get_obj_by_name(name)
        if(info == None):
            self.view.show_error("INVALID ADDRESS")
        else:
            self.view.show_object(info[3], info)

    def find_object_by_address(self):
        addr = self.view.get_object_address()
        info = self.model.get_obj_by_addr(addr)
        if(info == None):
            self.view.show_error("INVALID ADDRESS")
        else:
            self.view.show_object(addr, info)

    def copy_extracetd_data(self, hex_extractor_dto):
        for item in hex_extractor_dto:
            self.model.add_obj(item.address, item.name, item.section, item.location)

    def extract_map_file(self, map_file):

        mem_sections = self.model.get_mem_sections()
        reserved_words = self.model.get_reserved_words()
        extractor = map_extractor()
        return extractor.extract_map_file(map_file, mem_sections, reserved_words)

    def reload_map_file(self):
        try:
            map_file_path = self.view.get_file_location()
            (extractor_dto, map_parse_errors) = self.extract_map_file(map_file_path)
            self.copy_extracetd_data(extractor_dto)
            if(len(map_parse_errors) > 0):
                self.view.show_error(str(map_parse_errors))
        except Exception as ex:
            self.view.show_error(str(ex))


    def get_all(self):
        keys = self.model.get_all_addrs()
        for key in keys:
            obj_to_disp = self.model.get_obj_by_addr(key)
            self.view.show_object(key, obj_to_disp)

    def start(self):
        self.view.mainloop()

    def connect(self):
        pass

    def disconnect(self):
        pass

