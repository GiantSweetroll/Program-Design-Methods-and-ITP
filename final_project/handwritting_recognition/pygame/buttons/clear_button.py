from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.settings import Settings


class ClearButton(Button):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings, "Clear", button_color = (239, 43, 44))