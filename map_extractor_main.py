from simple_map_extractor_controller import MapExtractorController
from simple_map_extractor_model import MapExtractorModel
from tkView2 import TkView2
from pyserial_wrapper import *

memory_sections = [".text.", ".rodata.", ".bss.", ".data."]
reserved_words = ["*"]

communication = pyserial_wrapper('COM3', 115200)

extractor = MapExtractorController(view = TkView2(), model = MapExtractorModel(memory_sections, reserved_words), serial_com=communication)

extractor.start()