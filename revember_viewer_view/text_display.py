import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter import scrolledtext


class TextDisplay:

    def disp_controls_setup(self):
        self.dip_ctl_frame = tk.Frame(master=self.result_frame)
        self.clr_btn = tk.Button(master=self.dip_ctl_frame, command=self.erase_display, text="Clear")
        self.save_btn = tk.Button(master=self.dip_ctl_frame, command=self.save_to_file, text="save to file")
        self.ctl_lbl = tk.Label(master=self.dip_ctl_frame, text="overwrite")
        self.ovr_var = tk.BooleanVar()
        self.ctl_checkbox = tk.Checkbutton(master=self.dip_ctl_frame, variable=self.ovr_var)
        self.ctl_checkbox.pack(side=tk.LEFT)
        self.ctl_lbl.pack(side=tk.LEFT)
        self.clr_btn.pack(side = tk.RIGHT)
        self.save_btn.pack(side = tk.RIGHT)
        self.dip_ctl_frame.pack(side = tk.RIGHT)


    def __init__(self, title, master, position, width):
        self.result_frame = tk.Frame(master)
        self.result_label = tk.Label(master=self.result_frame, text=title)
        self.result_text = scrolledtext.ScrolledText(master=self.result_frame, width=width)
        self.result_label.pack()
        self.result_text.pack(expand=1, fill=tk.BOTH)
        self.disp_controls_setup()
        self.result_frame.grid(row = 0, column=position, rowspan=2, sticky='news')

    def save_to_file(self):
        files = [('All Files', '*.*'),   
            ('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files)
        file_content = self.result_text.get("1.0", tk.END)
        file.writelines(file_content)

    def show_text(self, text):
        if self.ovr_var.get() == 1:
            self.erase_display()
        self.result_text.insert(tk.END, text)

    def erase_display(self):
        self.result_text.delete("1.0", tk.END)