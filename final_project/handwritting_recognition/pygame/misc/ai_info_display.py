from final_project.handwritting_recognition import constants
from final_project.handwritting_recognition.pygame.misc.console import Console


class AIInfoDisplay(Console):
    
    #Constructor
    def __init__(self, path=constants.path_img_ai_info_empty):
        super().__init__(path)