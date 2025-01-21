import tkinter as tk

class TkView:
    def setup(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("map_extractor")


        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        self.generate_uuid_button = tk.Button(self.frame, text="get address", command=controller.process_new_data)
        self.generate_uuid_button.pack()        
        self.label = tk.Label(self.frame, text = "Result")
        self.label.pack()
        self.my_string_var = tk.StringVar()
        self.my_label = tk.Label(self.frame, textvariable= self.my_string_var)
        self.my_label.pack()


        self.my_string_var.set("dupa")

    def show_object(self, addr, object_properties):
        #(address, name, section, region, location)
        text = f"address: {hex(addr)} \n    name: {object_properties[0]} \n    section: {object_properties[1]} \n    location: {object_properties[2]}"
        self.my_string_var.set(text)

    def show_error(self):
        text = "ADDRESS NOT FOUND"
        self.my_string_var.set(text)

    def get_data(self):
        try:
            addr = int(self.entry.get(), 16)
            return addr
        except ValueError:
            self.my_string_var.set("INVALID VALUE")
            return None 

    def mainloop(self):
        self.root.mainloop()