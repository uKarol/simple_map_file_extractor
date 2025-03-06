import tkinter as tk
from tkinter import messagebox
from revember_viewer_view.text_display import TextDisplay
from revember_viewer_view.connection_panel import ConncetionPanel
from revember_viewer_view.control_panel import ControlPanel
import traceback
import sys

class RevemberViewer_TkView:

    def setup(self, controller):
        
        self.controller = controller
        self.root = tk.Tk()

        self.root.geometry("1050x600")
        self.root.title("map_extractor")
        self.control_panel = ControlPanel(self.root, 0, controller)
        self.result_disp = TextDisplay("result", self.root, 1, 40)
        self.info_disp = TextDisplay("info", self.root, 2, 60)
        self.connection_panel = ConncetionPanel(self.root, controller)
        self.root.rowconfigure((1,2),weight=1)
        self.activate_connect_btn()

    def open_file(self):
        self.control_panel.open_file()

    def erase_display(self):
        self.result_disp.erase_display()

    def get_file_location(self):
        return self.control_panel.get_file_path()

    def show_object(self, addr, object_properties):
        text = f"address: {hex(addr)} \n    name: {object_properties[0]} \n    section: {object_properties[1]} \n    location: {object_properties[2]} \n"
        self.result_disp.show_text(text)

    def show_info_object(self,text):
        self.info_disp.show_text(text)

    def show_error(self, error_desc = ""):
        messagebox.showerror("dziadostwo", error_desc)

    def get_reg_address(self):
        try:
            addr = int(self.control_panel.get_reg_address(), 16)
            return addr
        except ValueError:
            return None 

    def get_object_address(self):
        try:
            addr = int(self.control_panel.get_object_address(), 16)
            return addr
        except ValueError:
            return None 
        
    def get_object_name(self):
        try:
            name = self.control_panel.get_object_name()
            return name
        except ValueError:
            return None 
        
    def initial_open(self):
        self.open_file()
        self.controller.get_and_reload_map_file()

    def get_connection_params(self):
        return self.connection_panel.get_connection_params()
    
    def close_window(self):
        self.root.destroy()

    def show_error_in_console(self, error, location):
        trash, trash2, tb = sys.exc_info()
        print(f"PROBLEM OCCURED IN {location}")
        traceback.print_tb(tb)

    def mainloop(self):
        self.root.protocol("WM_DELETE_WINDOW", self.controller.on_close)
        self.root.after(1, self.initial_open)
        self.root.mainloop()
    
    def activate_connect_btn(self):
        self.connection_panel.activate_connect_button()
        self.connection_panel.disable_disconnect_button()

    def activate_disconnect_btn(self):
        self.connection_panel.activate_disconnect_button()
        self.connection_panel.disable_connect_button()
