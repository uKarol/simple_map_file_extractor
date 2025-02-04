from DTO_test import *

class map_extractor:

    def __init__(self, mem_sections, reserved_strings, dto_list: list):
        self.sections = mem_sections
        self.map_errors = []
        self.reserved_strings = reserved_strings
        self.extracted_values = []
        self.dto_list = dto_list

    def get_errors(self):
        return self.map_errors

    def one_line_split(self, line : list):
        try: 
            full_name = line[0].split('.')
            addr = int(line[1], 16)
            location = line[3]
            section = full_name[1]
            name = full_name[2]
            self.dto_list.append(UserDTO_data(addr, name, section, location))
        except Exception as es:
            self.map_errors.append(str(es))

    def two_line_split(self, line1 : list, line2 : list):
        try:
            full_name = line1[0].split('.')
            addr = int(line2[0], 16)
            location = line2[2]
            section = full_name[1]
            name = full_name[2]
            self.dto_list.append(UserDTO_data(addr, name, section, location))
        except Exception as es:
            self.map_errors.append(str(es))

    def validate_line(self, line):
        if any(word in line for word in self.sections):
            if not any(invalid_str in line for invalid_str in self.reserved_strings ):
                return line.split()
        return []

    def extract_map_file(self, map_file):
        with open(map_file, mode='r') as file:
            lines = file.readlines()
            myiter = iter(lines)
            for line in myiter:
                splitted_line = self.validate_line(line)
                if len(splitted_line) > 1:
                    #in one line
                    self.one_line_split(line.split())
                elif len(splitted_line) == 1:
                    #in two lines
                    splitted_line2 = (next(myiter)).split()
                    self.two_line_split(splitted_line, splitted_line2)
