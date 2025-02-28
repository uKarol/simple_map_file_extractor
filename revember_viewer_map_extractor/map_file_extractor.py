from revember_viewer_model.DTO_test import *

class map_extractor:

    def __init__(self):
        pass

    def one_line_split(self, line : list, dto_list, map_errors):
        try: 
            full_name = line[0].split('.')
            addr = int(line[1], 16)
            location = line[3]
            section = full_name[1]
            name = full_name[2]
            if(addr != 0):
                dto_list.append(UserDTO_data(addr, name, section, location))
        except Exception as es:
            map_errors.append(str(es))

    def two_line_split(self, line1 : list, line2 : list, dto_list, map_errors):
        try:
            full_name = line1[0].split('.')
            addr = int(line2[0], 16)
            location = line2[2]
            section = full_name[1]
            name = full_name[2]
            if(addr != 0):
                dto_list.append(UserDTO_data(addr, name, section, location))
        except Exception as es:
            map_errors.append(str(es))

    def validate_line(self, line, mem_sections, reserved_strings):
        if any(word in line for word in mem_sections):
            if not any(invalid_str in line for invalid_str in reserved_strings ):
                return line.split()
        return []

    def extract_map_file(self, map_file, mem_sections, reserved_strings):
        map_errors = []
        dto_list = []
        with open(map_file, mode='r') as file:
            lines = file.readlines()
            myiter = iter(lines)
            for line in myiter:
                splitted_line = self.validate_line(line, mem_sections, reserved_strings)
                if len(splitted_line) > 1:
                    #in one line
                    self.one_line_split(line.split(), dto_list, map_errors)
                elif len(splitted_line) == 1:
                    #in two lines
                    splitted_line2 = (next(myiter)).split()
                    self.two_line_split(splitted_line, splitted_line2, dto_list, map_errors)
        return(dto_list, map_errors)