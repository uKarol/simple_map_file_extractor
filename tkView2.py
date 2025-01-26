import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


class TkView2:

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
        self.address_btn = tk.Button(master = self.address_frame, text="get address", command = self.controller.process_new_data)
        self.address_label = tk.Label(master = self.address_frame, text="object address")
        self.address_label.pack()
        self.address_entry.pack(side=tk.LEFT)
        self.address_btn.pack(side=tk.RIGHT)
        self.address_frame.pack()

    def setup_result_display(self):
        self.result_frame = tk.Frame(master=self.root)
        self.result_label = tk.Label(master=self.result_frame, text="result")
        self.result_text = tk.Text(master=self.result_frame)
        self.result_label.pack()
        self.result_text.pack(expand=1, fill=tk.BOTH)
        self.result_frame.pack(expand=1, fill=tk.BOTH)
        
    def disp_controls_setup(self):
        self.dip_ctl_frame = tk.Frame(master=self.control_frame)
        self.clr_btn = tk.Button(master=self.dip_ctl_frame, command=self.erase_display, text="Clear")
        self.ctl_lbl = tk.Label(master=self.dip_ctl_frame, text="overwrite")
        self.ovr_var = tk.BooleanVar()
        self.ctl_checkbox = tk.Checkbutton(master=self.dip_ctl_frame, variable=self.ovr_var)
        self.ctl_checkbox.pack(side=tk.LEFT)
        self.ctl_lbl.pack(side=tk.LEFT)
        self.clr_btn.pack(side = tk.RIGHT)
        self.dip_ctl_frame.pack(side = tk.RIGHT)

    def setup(self, controller):
        
        self.controller = controller
        self.root = tk.Tk()
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(side = tk.LEFT)
        self.root.geometry("600x400")
        self.root.title("map_extractor")
        self.setup_address_entry()
        self.setup_file_finder()
        self.disp_controls_setup()
        self.setup_result_display()

    def erase_display(self):
        self.result_text.delete("1.0", tk.END)

    def get_file_location(self):
        return self.filepath_entry.get()

    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("Map Files", "*.map"), ("All Files", "*.*")]
        )
        self.file_string_var.set(filepath)
        print(filepath)

    def show_object(self, addr, object_properties):
        if self.ovr_var.get() == 1:
            self.erase_display()
        text = f"address: {hex(addr)} \n    name: {object_properties[0]} \n    section: {object_properties[1]} \n    location: {object_properties[2]} \n"
        self.result_text.insert(tk.END, text)

    def show_error(self, error_decs = ""):
        messagebox.showerror("dziadostwo", error_decs)

    def get_data(self):
        try:
            addr = int(self.address_entry.get(), 16)
            return addr
        except ValueError:
            return None 

    def mainloop(self):
        self.root.mainloop()
