class MapFileObjects:

    def __init__(self, name, section, location, address):
            self.name = name
            self.section = section
            self.location = location
            self.address = address
            

    def get_object_info(self):
        return [self.name, self.section, self.location, self.address]

class MapExtractorModel:
    
    def __init__(self, mem_sections, reserved_words):
        self.objdict_addr = {}
        self.objdict_name = {}
        self.addr_list = []
        self.sections = mem_sections
        self.reserved_words = reserved_words

    def get_mem_sections(self):
        return self.sections

    def get_reserved_words(self):
        return self.reserved_words
    
    def add_obj(self, address, name, section, location):
        self.objdict_addr.update({address: MapFileObjects(name, section, location, address)})
        self.objdict_name.update({name: MapFileObjects(name, section, location, address)})
        self.addr_list.append(address)

    def get_all_addrs(self):
        return self.objdict_addr.keys()
    
    def get_nearest_object(self, reg_addr):
        myiter = iter(self.addr_list)
        for addr in myiter:
            if next(myiter) > reg_addr:
                return self.get_obj_by_addr(addr)
        return None

    def get_obj_by_name(self, name):
        try:
            return self.objdict_name[name].get_object_info()
        except KeyError:
            return None

    def get_obj_by_addr(self, address):
        try:
            return self.objdict_addr[address].get_object_info()
        except KeyError:
            return None