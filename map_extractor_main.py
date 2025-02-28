from simple_map_extractor_controller import MapExtractorController
from revember_viewer_model.simple_map_extractor_model import MapExtractorModel
from revember_viewer_view.tkView2 import TkView2
from revember_viewer_aux.pyserial_wrapper import *

memory_sections = [".text.", ".rodata.", ".bss.", ".data."]
reserved_words = ["*"]

communication = pyserial_wrapper()
extractor = MapExtractorController(view = TkView2(), model = MapExtractorModel(memory_sections, reserved_words), serial_com=communication)

extractor.start()