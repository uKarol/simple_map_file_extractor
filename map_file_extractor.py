    
class map_extractor:

    def __init__(self, model):
        self.model = model

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
        
        sections = self.model.get_mem_sections()
        reserved_strings = []
        with open(map_file, mode='r') as file:
            lines = file.readlines()
            myiter = iter(lines)
            for line in myiter:
                if any(word in line for word in sections):
                    splitted_line = line.split()
                    if len(splitted_line) > 1:
                        #in one line
                        self.one_line_split(line.split())
                    elif len(splitted_line) == 1:
                        #in two lines
                        splitted_line2 = (next(myiter)).split()
                        self.two_line_split(splitted_line, splitted_line2)
