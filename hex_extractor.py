class MapFileObjects:

    def __init__(self, name, section, location):
            self.name = name
            self.section = section
            self.location = location

    def get_object_info(self):
        return [self.name, self.section, self.location]

class MapExtractorModel:
    
    def __init__(self):
        self.objdict = {} 
    
    def add_obj(self, address, name, section, location):
        self.objdict.update({address: MapFileObjects(name, section, location)})

    def get_all_addrs(self):
        return self.objdict.keys()

    def get_obj_by_addr(self, address):
        try:
            return self.objdict[address].get_object_info()
        except KeyError:
            return None

class MapExtractorView:

    def __init__(self):
        pass

    def setup(self, controller):
        self.controller = controller

    def show_object(self, addr, object_properties):
        #(address, name, section, region, location)
        print(f"address: {hex(addr)} \n    name: {object_properties[0]} \n    section: {object_properties[1]} \n    location: {object_properties[2]}")

    def show_error(self):
        print("ADDRESS NOT FOUND")

    def mainloop(self):
        while(True):
            x = input("write_address: ")
            try:
                addr = int(x, 16)
                self.controller.process_new_data(addr)
            except ValueError:
                print("INVALID VALUE")

            

class MapExtractorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setup(self)

    def process_new_data(self, addr):
        info = self.model.get_obj_by_addr(addr)
        if(info == None):
            self.view.show_error()
        else:
            self.view.show_object(addr, info)

    def one_line_split(self, line : list):
        full_name = line[0].split('.')
        addr = int(line[1], 16)
        location = line[3]
        section = full_name[1]
        name = full_name[2]
        self.model.add_obj(addr, name, section, location)


    def two_line_split(self, line1 : list, line2 : list):
        full_name = line1[0].split('.')
        addr = int(line2[0], 16)
        location = line2[2]
        section = full_name[1]
        name = full_name[2]
        self.model.add_obj(addr, name, section, location)

    def extract_map_file(self, map_file):
        
        substrings = [".text.", ".rodata.", ".bss.", ".data."]
        with open(map_file, mode='r') as file:
            lines = file.readlines()
            myiter = iter(lines)
            for line in myiter:
                if any(word in line for word in substrings):
                    if not '0x' in line:
                        #in two lines
                        line1 = line.split()
                        line2 = (next(myiter)).split()
                        self.two_line_split(line1, line2)
                    else:
                        #in one line
                        self.one_line_split(line.split())

    def get_all(self):
        keys = self.model.get_all_addrs()
        for key in keys:
            obj_to_disp = self.model.get_obj_by_addr(key)
            self.view.show_object(key, obj_to_disp)

    def start(self):
        self.view.mainloop()



extractor = MapExtractorController(view = MapExtractorView(), model = MapExtractorModel())



extractor.extract_map_file("first_project.map")

extractor.get_all()
extractor.start()