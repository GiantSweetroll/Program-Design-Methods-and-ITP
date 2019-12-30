from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.settings import Settings


class ExitButton(Button):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings, "Exit", button_color = (239, 43, 44))