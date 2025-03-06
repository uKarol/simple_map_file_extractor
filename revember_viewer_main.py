from revember_viewer_controller import RevemberViewerController
from revember_viewer_model.simple_map_extractor_model import MapExtractorModel
from revember_viewer_view.revember_viewer_tkview import RevemberViewer_TkView
from revember_viewer_aux.pyserial_wrapper import *

memory_sections = [".text.", ".rodata.", ".bss.", ".data."]
reserved_words = ["*"]

communication = pyserial_wrapper()
extractor = RevemberViewerController(view = RevemberViewer_TkView(), model = MapExtractorModel(memory_sections, reserved_words), serial_com=communication)

extractor.start()