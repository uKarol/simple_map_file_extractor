from revember_viewer_map_extractor.map_file_extractor import map_extractor
from revember_viewer_model.DTO_test import *
from revember_viewer_msg_decoder.HeaderDecoder import *
from revember_viewer_msg_decoder.GlobalDecoder import *
from revember_viewer_aux.thread_interface import *

import struct
import time
class RevemberViewerController:

    def __init__(self, model, view, serial_com):
        self.model = model
        self.thread_active = True
        self.view = view
        self.view.setup(self)
        self.hex_extractor_dto = []
        self.task_ctl = TaskController(self.process_received_data)
        self.serial_com = serial_com
        self.connected = False

        self.map_getter = MapDetailsGetter(self.model.get_obj_by_addr, self.model.get_nearest_object)
        self.decoder = GenericDataDecoder(self.map_getter)
        self.reader = HeaderDecoder(self.serial_com)

    def process_received_data(self):
        try:
            (my_packet, data) = self.reader.receive_packet()
            if(my_packet != None):
                ret_val = self.decoder.decode(my_packet, data)
                self.view.show_info_object(ret_val)

        except TypeError as ex:
            self.controller_exception_handler(ex, "process_received_data task")

        except struct.error as ex:
            self.controller_exception_handler(ex, "process_received_data task")

        except HeaderReceptionError as ex:
            self.controller_exception_handler(ex, "process_received_data task")
            self.view.show_info_object("PROBLEM DURING DATA RECEPTION")

        except ConnectionError as ex:
            self.controller_exception_handler(ex, "process_received_data task")

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
        self.model.clear_model()
        map_file_path = self.view.get_file_location()
        self.reload_map_file(map_file_path)


    def reload_map_file(self, filepath):
        try:
            (extractor_dto, map_parse_errors) = self.extract_map_file(filepath)
            self.copy_extracetd_data(extractor_dto)
            if(len(map_parse_errors) > 0):
                self.view.show_error(str(map_parse_errors))
        except FileNotFoundError as ex:     
            self.controller_exception_handler(ex, "reloading map file")

    def get_all(self):
        keys = self.model.get_all_addrs()
        for key in keys:
            obj_to_disp = self.model.get_obj_by_addr(key)
            self.view.show_object(key, obj_to_disp)

    def start(self):
        self.task_ctl.start_task()
        self.view.mainloop()

    def on_close(self):
        self.task_ctl.finish_task()
        self.view.close_window()
    
    #in case of any error: suspend task, disconnect serial, print traceback in console
    def controller_exception_handler(self, ex : Exception, location : str):
        try:
            self._disconnect_and_suspend_task()
        except:
            pass #suppress exceptions here - prevent recursion
        self.view.show_error_in_console(ex, location)

    def connect(self):
        try:
            [speed, port_com] = self.view.get_connection_params()
            self.serial_com.connect(port_com, int(speed))
            self.decoder.reset_indentation()
            
        except ConnectionError as ex:
            self.view.show_error("SerialException \n"+ str(ex))
            self.controller_exception_handler(ex, "CONNECT BTN CALLBACK")
        else:
            self.task_ctl.resume_task()
            self.view.activate_disconnect_btn()

    def _disconnect_and_suspend_task(self):
        self.task_ctl.suspend_task()
        time.sleep(0.1)
        self.serial_com.disconnect()
        self.view.activate_connect_btn()

    def disconnect(self):
        try:
            self._disconnect_and_suspend_task()
        except ConnectionError as ex:
            self.controller_exception_handler(ex, "DISCONNECT BUTTON CALLBACK")

