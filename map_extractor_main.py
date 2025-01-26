from simple_map_extractor_cliview import MapExtractorCliView
from simple_map_extractor_controller import MapExtractorController
from simple_map_extractor_model import MapExtractorModel
from simple_map_extractor_tkView import TkView
from tkView2 import TkView2

extractor = MapExtractorController(view = TkView2(), model = MapExtractorModel())

extractor.start()