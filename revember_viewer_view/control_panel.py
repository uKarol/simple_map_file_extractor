import tkinter as tk
from tkinter.filedialog import askopenfilename


class ControlPanel:

    def __init__(self, master, controller):
        self.controller = controller
        self.control_frame = master
        self.setup_file_finder()
        self.setup_address_entry()
        self.indetation_ctl_setup()
        
    def auto_indent_is_active(self):
        return self.auto_indent_var.get()

    def setup_file_finder(self):
        self.file_finder_frame = tk.Frame(self.control_frame)

        self.file_string_var = tk.StringVar()
        self.file_finder_label = tk.Label(master=self.file_finder_frame, text="Map File Location")
        self.file_finder_label.pack()
        self.filepath_entry = tk.Entry(self.file_finder_frame, textvariable=self.file_string_var)
        self.filepath_entry.pack(side=tk.LEFT)
        self.filepath_btn = tk.Button(self.file_finder_frame, text="...", command=self.open_file)
        self.reload_btn = tk.Button(self.file_finder_frame, text="reload", command=self.controller.get_and_reload_map_file)

        self.filepath_btn.pack(side=tk.LEFT)
        self.reload_btn.pack(side=tk.RIGHT)
        self.file_finder_frame.pack(side=tk.TOP)
        self.file_string_var.set("first_project.map")

    def indetation_ctl_setup(self):
        self.idnt_frame = tk.Frame(master = self.control_frame)
        self.indent_clear_btn = tk.Button(master = self.idnt_frame, text="reset_indantation", command = self.controller.reset_indantation)
        self.idnt_frame.pack(side=tk.BOTTOM)
        self.auto_indent_var = tk.BooleanVar()
        self.auto_indent_var.set(True)
        self.ctl_checkbox = tk.Checkbutton(master=self.idnt_frame, variable=self.auto_indent_var, text="auto indentation", command=self.set_indentation)
        self.ctl_checkbox.pack()
        self.indent_clear_btn.pack()

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

    def set_indentation(self):
        if self.auto_indent_var.get():
            self.controller.enable_auto_indentation()
        else:
            self.controller.disable_auto_indentation()

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
