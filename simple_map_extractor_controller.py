from map_file_extractor import map_extractor

class MapExtractorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setup(self)
        self.extractor = map_extractor(self.model)

    def process_new_data(self):
        addr = self.view.get_data()
        info = self.model.get_obj_by_addr(addr)
        if(info == None):
            self.view.show_error("INVALID ADDRESS")
        else:
            self.view.show_object(addr, info)

    def extract_map_file(self, map_file):
        self.extractor.extract_map_file(map_file)

    def reload_map_file(self):
        try:
            map_file_path = self.view.get_file_location()
            self.extract_map_file(map_file_path)
        except:
            self.view.show_error("problem with map file")

    def get_all(self):
        keys = self.model.get_all_addrs()
        for key in keys:
            obj_to_disp = self.model.get_obj_by_addr(key)
            self.view.show_object(key, obj_to_disp)

    def start(self):
        self.view.mainloop()