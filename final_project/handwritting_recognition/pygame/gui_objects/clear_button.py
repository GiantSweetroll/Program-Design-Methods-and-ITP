from final_project.handwritting_recognition.pygame.gui_objects.button import Button

class ClearButton(Button):
    
    #Constructor
    def __init__(self, screen):
        super().__init__(screen, "Clear", button_color = (239, 43, 44))
        self.get_rect().right = screen.get_rect().right - 20
        self.get_rect().centery = screen.get_rect().bottom - self.height
        self.prep_msg(self.get_text())