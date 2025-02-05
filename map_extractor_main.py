from simple_map_extractor_controller import MapExtractorController
from simple_map_extractor_model import MapExtractorModel
from tkView2 import TkView2

memory_sections = [".text.", ".rodata.", ".bss.", ".data."]
reserved_words = ["*"]

extractor = MapExtractorController(view = TkView2(), model = MapExtractorModel(memory_sections, reserved_words))

extractor.start()