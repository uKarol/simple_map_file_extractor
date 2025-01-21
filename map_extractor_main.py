from simple_map_extractor_cliview import MapExtractorCliView
from simple_map_extractor_controller import MapExtractorController
from simple_map_extractor_model import MapExtractorModel
from simple_map_extractor_tkView import TkView


extractor = MapExtractorController(view = TkView(), model = MapExtractorModel())

extractor.extract_map_file("first_project.map")

extractor.get_all()
extractor.start()