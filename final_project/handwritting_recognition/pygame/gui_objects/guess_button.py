from final_project.handwritting_recognition.pygame.gui_objects.button import Button

class GuessButton(Button):
    
    #Constructor
    def __init__(self, screen):
        super().__init__(screen, "Guess")
        self.get_rect().centery = screen.get_rect().bottom - self.height
        self.prep_msg(self.get_text())