import tkinter as tk
from tkinter import scrolledtext


class StatusLog:

    def disp_controls_setup(self):
        self.dip_ctl_frame = tk.Frame(master=self.result_frame)
        self.clr_btn = tk.Button(master=self.dip_ctl_frame, command=self.erase_display, text="Clear")
        self.clr_btn.pack(side = tk.RIGHT)
        self.dip_ctl_frame.pack(side = tk.RIGHT)


    def __init__(self, title, master):
        self.result_frame = master
        self.result_label = tk.Label(master=self.result_frame, text=title)
        self.result_text = scrolledtext.ScrolledText(master=self.result_frame, height= 3)
        self.result_label.pack()
        self.result_text.pack(expand=1, fill=tk.BOTH)
        self.disp_controls_setup()


    def show_text(self, text):
        self.result_text.insert(tk.END, text)
        self.result_text.yview(tk.END)

    def erase_display(self):
        self.result_text.delete("1.0", tk.END)