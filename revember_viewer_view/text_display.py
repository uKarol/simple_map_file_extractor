import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter import scrolledtext


class TextDisplay:

    def disp_controls_setup(self):
        self.dip_ctl_frame = tk.Frame(master=self.result_frame)
        self.clr_btn = tk.Button(master=self.dip_ctl_frame, command=self.erase_display, text="Clear")
        self.save_btn = tk.Button(master=self.dip_ctl_frame, command=self.save_to_file, text="save to file")
        self.ovr_var = tk.BooleanVar()
        self.ctl_checkbox = tk.Checkbutton(master=self.dip_ctl_frame, variable=self.ovr_var, text="overwrite")
        self.ctl_checkbox.pack(side=tk.LEFT)
        self.clr_btn.pack(side = tk.RIGHT)
        self.save_btn.pack(side = tk.RIGHT)
        self.dip_ctl_frame.pack(side = tk.RIGHT)


    def __init__(self, title, master, width):
        self.result_frame = master
        self.result_label = tk.Label(master=self.result_frame, text=title)
        textContainer = tk.Frame(self.result_frame, borderwidth=1, relief="sunken")
        self.result_text = tk.Text(textContainer, width=width, wrap = "none")
        textVsb = tk.Scrollbar(textContainer, orient="vertical", command=self.result_text.yview)
        textHsb = tk.Scrollbar(textContainer, orient="horizontal", command=self.result_text.xview)
        self.result_text.configure(yscrollcommand=textVsb.set, xscrollcommand=textHsb.set)
        self.result_label.pack()
        textContainer.pack(expand=1, fill=tk.BOTH)
        self.result_text.grid(row=0, column=0, sticky="nsew")
        textVsb.grid(row=0, column=1, sticky="ns")
        textHsb.grid(row=1, column=0, sticky="ew")

        textContainer.grid_rowconfigure(0, weight=1)
        textContainer.grid_columnconfigure(0, weight=1)
        self.disp_controls_setup()


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
        self.result_text.yview(tk.END)

    def erase_display(self):
        self.result_text.delete("1.0", tk.END)