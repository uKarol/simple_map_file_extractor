class MapExtractorCliView:

    def __init__(self):
        self.data = None

    def setup(self, controller):
        self.controller = controller

    def show_object(self, addr, object_properties):
        #(address, name, section, region, location)
        print(f"address: {hex(addr)} \n    name: {object_properties[0]} \n    section: {object_properties[1]} \n    location: {object_properties[2]}")

    def show_error(self):
        print("ADDRESS NOT FOUND")

    def get_object_address(self):
        try:
            addr = int(self.data, 16)
            return addr
        except ValueError:
            print("INVALID VALUE")
            return None 

    def mainloop(self):
        while(True):
            self.data = input("write_address: ")
            try:
                self.controller.find_object_by_address()
            except ValueError:
                print("INVALID VALUE")