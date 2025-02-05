import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class TextDisplay:

    def disp_controls_setup(self):
        self.dip_ctl_frame = tk.Frame(master=self.result_frame)
        self.clr_btn = tk.Button(master=self.dip_ctl_frame, command=self.erase_display, text="Clear")
        self.ctl_lbl = tk.Label(master=self.dip_ctl_frame, text="overwrite")
        self.ovr_var = tk.BooleanVar()
        self.ctl_checkbox = tk.Checkbutton(master=self.dip_ctl_frame, variable=self.ovr_var)
        self.ctl_checkbox.pack(side=tk.LEFT)
        self.ctl_lbl.pack(side=tk.LEFT)
        self.clr_btn.pack(side = tk.RIGHT)
        self.dip_ctl_frame.pack(side = tk.RIGHT)


    def __init__(self, title, master, position):
        self.result_frame = tk.Frame(master)
        self.result_label = tk.Label(master=self.result_frame, text=title)
        self.result_text = tk.Text(master=self.result_frame, width=40)
        self.result_label.pack()
        self.result_text.pack(expand=1, fill=tk.BOTH)
        self.disp_controls_setup()
        self.result_frame.grid(row = 0, column=position, rowspan=2, sticky='news')

    def show_text(self, text):
        if self.ovr_var.get() == 1:
            self.erase_display()
        self.result_text.insert(tk.END, text)

    def erase_display(self):
        self.result_text.delete("1.0", tk.END)

class Conncetion_Panel:
    
    def __init__(self, master, controller):

        self.controller = controller

        self.con_frame = tk.Frame(master)
        self.port_entry = tk.Entry(self.con_frame)
        self.port_entry.grid(row=0, column=0)
        self.port_lbl = tk.Label(self.con_frame, text="PORT COM")
        self.port_lbl.grid(row=0, column=1)

        self.speed_entry = tk.Entry(self.con_frame)
        self.speed_entry.grid(row=1, column=0)
        self.speed_lbl = tk.Label(self.con_frame, text="SPEED")
        self.speed_lbl.grid(row=1, column=1)

        self.connect_button = tk.Button(self.con_frame, text="CONNECT", command= self.controller.connect)
        self.connect_button.grid(row=2, column=0)
        self.disconnect_button = tk.Button(self.con_frame, text="DISCONNECT", command= self.controller.disconnect)
        self.disconnect_button.grid(row=2, column=1)

        self.con_frame.grid(row=1, column=0)

    def get_connection_params(self):
        return [self.speed_entry.get(), self.port_entry.get()]
    
    

class ControlPanel:
    
    def __init__(self, master, position, controller):
        self.controller = controller
        self.control_frame = tk.Frame(master)
        self.setup_file_finder()
        self.setup_address_entry()
        self.control_frame.grid(row = position, column=0)
        

    def setup_file_finder(self):
        self.file_finder_frame = tk.Frame(self.control_frame)

        self.file_string_var = tk.StringVar()
        self.file_finder_label = tk.Label(master=self.file_finder_frame, text="Map File Location")
        self.file_finder_label.pack()
        self.filepath_entry = tk.Entry(self.file_finder_frame, textvariable=self.file_string_var)
        self.filepath_entry.pack(side=tk.LEFT)
        self.filepath_btn = tk.Button(self.file_finder_frame, text="...", command=self.open_file)
        self.reload_btn = tk.Button(self.file_finder_frame, text="reload", command=self.controller.reload_map_file)

        self.filepath_btn.pack(side=tk.LEFT)
        self.reload_btn.pack(side=tk.RIGHT)
        self.file_finder_frame.pack(side=tk.TOP)
        self.file_string_var.set("first_project.map")

    def setup_address_entry(self):
        self.address_frame = tk.Frame(master = self.control_frame)
        self.address_entry = tk.Entry(master = self.address_frame)
        self.address_btn = tk.Button(master = self.address_frame, text="get", command = self.controller.find_object_by_address)
        self.address_label = tk.Label(master = self.address_frame, text="object by address")
        self.address_label.pack()
        self.address_entry.pack(side=tk.LEFT)
        self.address_btn.pack(side=tk.RIGHT)
        self.address_frame.pack()
    
        self.name_frame = tk.Frame(master = self.control_frame)
        self.name_entry = tk.Entry(master = self.name_frame)
        self.name_btn = tk.Button(master = self.name_frame, text="get", command = self.controller.find_object_by_name)
        self.name_label = tk.Label(master = self.name_frame, text="object by name")
        self.name_label.pack()
        self.name_entry.pack(side=tk.LEFT)
        self.name_btn.pack(side=tk.RIGHT)
        self.name_frame.pack()

        self.reg_frame = tk.Frame(master = self.control_frame)
        self.reg_entry = tk.Entry(master = self.reg_frame)
        self.reg_btn = tk.Button(master = self.reg_frame, text="get", command = self.controller.find_nearest_object)
        self.reg_label = tk.Label(master = self.reg_frame, text="object by LR or PC")
        self.reg_label.pack()
        self.reg_entry.pack(side=tk.LEFT)
        self.reg_btn.pack(side=tk.RIGHT)
        self.reg_frame.pack()

    def get_reg_address(self):
        return self.reg_entry.get()

    def get_file_path(self):
        return self.filepath_entry.get()
    
    def set_file_path(self, filepath):
        self.file_string_var.set(filepath)

    def get_object_address(self): 
        return self.address_entry.get()
    
    def get_object_name(self): 
        return self.name_entry.get()

    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("Map Files", "*.map"), ("All Files", "*.*")]
        )
        self.set_file_path(filepath)
        print(filepath)

class TkView2:

    def setup(self, controller):
        
        self.controller = controller
        self.root = tk.Tk()

        self.root.geometry("900x600")
        self.root.title("map_extractor")
        self.control_panel = ControlPanel(self.root, 0, controller)
        self.result_disp = TextDisplay("result", self.root, 1)
        self.info_disp = TextDisplay("info", self.root, 2)
        self.connection = Conncetion_Panel(self.root, controller)
        self.root.rowconfigure((1,2),weight=1)

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

    def mainloop(self):
        self.root.mainloop()
