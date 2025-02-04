from map_file_extractor import map_extractor
from DTO_test import *

class MapExtractorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setup(self)
        mem_sections = self.model.get_mem_sections()
        reserved_words = self.model.get_reserved_words()
        self.hex_extractor_dto = []
        self.extractor = map_extractor(mem_sections, reserved_words, self.hex_extractor_dto)

    def process_new_data(self):
        addr = self.view.get_data()
        info = self.model.get_obj_by_addr(addr)
        if(info == None):
            self.view.show_error("INVALID ADDRESS")
        else:
            self.view.show_object(addr, info)

    def copy_extracetd_data(self):
        for item in self.hex_extractor_dto:
            self.model.add_obj(item.address, item.name, item.section, item.location)
            #print(item)

    def extract_map_file(self, map_file):
        self.extractor.extract_map_file(map_file)
        return self.extractor.get_errors()

    def reload_map_file(self):
        try:
            map_file_path = self.view.get_file_location()
            map_parse_errors = self.extract_map_file(map_file_path)
            self.copy_extracetd_data()
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