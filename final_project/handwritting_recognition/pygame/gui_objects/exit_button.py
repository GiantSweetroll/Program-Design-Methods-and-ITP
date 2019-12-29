from final_project.handwritting_recognition.pygame.gui_objects.button import Button

class ExitButton(Button):
    
    #Constructor
    def __init__(self, screen):
        super().__init__(screen, "Exit", button_color = (239, 43, 44))
        self.get_rect().left = screen.get_rect().left + 20
        self.get_rect().centery = screen.get_rect().bottom - self.height
        self.prep_msg(self.get_text())