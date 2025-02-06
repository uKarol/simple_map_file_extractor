from simple_map_extractor_controller import MapExtractorController
from simple_map_extractor_model import MapExtractorModel
from tkView2 import TkView2
from pyserial_wrapper import *
from tkinter.filedialog import askopenfilename

memory_sections = [".text.", ".rodata.", ".bss.", ".data."]
reserved_words = ["*"]

communication = pyserial_wrapper()

extractor = MapExtractorController(view = TkView2(), model = MapExtractorModel(memory_sections, reserved_words), serial_com=communication)

filepath = askopenfilename(filetypes=[("Map Files", "*.map"), ("All Files", "*.*")])
extractor.reload_map_file(filepath)

extractor.start()