from map_file_extractor import map_extractor
from DTO_test import *

from param_decoder import *
from GlobalDecoder import *

from thread_interface import *

class MapExtractorController:

    def __init__(self, model, view, serial_com):
        self.model = model
        self.thread_active = True
        self.view = view
        self.view.setup(self)
        self.hex_extractor_dto = []
        self.task_ctl = TaskController(self.process_received_data)
        self.serial_com = serial_com
        self.connected = False

    def process_received_data(self):
        map_getter = MapDetailsGetter(self.model.get_obj_by_addr, self.model.get_nearest_object)
        decoder = GlobalHandler(map_getter)
        reader = packet_reader(self.serial_com)
        while(True):
            if(self.connected):
                try:
                    (my_packet, data) = reader.receive_packet()
                    ret_val = decoder.decoder(my_packet, data)
                    self.view.show_info_object(ret_val)
                except Exception as ex:
                    self.view.show_error(str(ex))

    def find_object_by_name(self):
        name = self.view.get_object_name()
        info = self.model.get_obj_by_name(name)
        if(info == None):
            self.view.show_error("NOT FOUND")
        else:
            self.view.show_object(info[3], info)

    def find_object_by_address(self):
        addr = self.view.get_object_address()
        info = self.model.get_obj_by_addr(addr)
        if(info == None):
            self.view.show_error("NOT FOUND")
        else:
            self.view.show_object(addr, info)

    def find_nearest_object(self):
        reg_addr = self.view.get_reg_address()
        info = self.model.get_nearest_object(reg_addr)
        if(info == None):
            self.view.show_error("NOT FOUND")
        else:
            self.view.show_object(info[3], info)

    def copy_extracetd_data(self, hex_extractor_dto):
        for item in hex_extractor_dto:
            self.model.add_obj(item.address, item.name, item.section, item.location)

    def extract_map_file(self, map_file):

        mem_sections = self.model.get_mem_sections()
        reserved_words = self.model.get_reserved_words()
        extractor = map_extractor()
        return extractor.extract_map_file(map_file, mem_sections, reserved_words)

    def get_and_reload_map_file(self):
        map_file_path = self.view.get_file_location()
        self.reload_map_file(map_file_path)


    def reload_map_file(self, filepath):
        try:
            (extractor_dto, map_parse_errors) = self.extract_map_file(filepath)
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
        self.task_ctl.start_task()
        self.view.mainloop()

    def connect(self):
        try:
            self.serial_com.connect('COM3', 115200)
            self.connected = True
        except Exception as ex:
            self.view.show_error(str(ex))

    def disconnect(self):
        self.serial_com.disconnect()
        self.connected = False

