import tkinter as tk

class ConncetionPanel:
    
    def __init__(self, master, controller):

        self.controller = controller
        self.port_var = tk.StringVar(value="COM3")
        self.con_frame = tk.Frame(master)
        self.port_entry = tk.Entry(self.con_frame, textvariable=self.port_var)
        self.port_entry.grid(row=0, column=0)
        self.port_lbl = tk.Label(self.con_frame, text="PORT COM")
        self.port_lbl.grid(row=0, column=1)

        self.speed_var = tk.StringVar(value="115200")
        self.speed_entry = tk.Entry(self.con_frame, textvariable=self.speed_var)
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
    
    def activate_connect_button(self):
        self.connect_button.config(state=tk.NORMAL)

    def disable_connect_button(self):
        self.connect_button.config(state=tk.DISABLED)

    def activate_disconnect_button(self):
        self.disconnect_button.config(state=tk.NORMAL)

    def disable_disconnect_button(self):
        self.disconnect_button.config(state=tk.DISABLED)