class MapFileObjects:

    def __init__(self, name, section, location):
            self.name = name
            self.section = section
            self.location = location

    def get_object_info(self):
        return [self.name, self.section, self.location]

class MapExtractorModel:
    
    def __init__(self, mem_sections):
        self.objdict = {}
        self.sections = mem_sections

    def get_mem_sections(self):
        return self.sections
    
    def add_obj(self, address, name, section, location):
        self.objdict.update({address: MapFileObjects(name, section, location)})

    def get_all_addrs(self):
        return self.objdict.keys()

    def get_obj_by_addr(self, address):
        try:
            return self.objdict[address].get_object_info()
        except KeyError:
            return None