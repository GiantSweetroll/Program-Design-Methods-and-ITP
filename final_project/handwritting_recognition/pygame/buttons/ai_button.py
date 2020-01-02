from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.data_drivers.ai import AI
from final_project.handwritting_recognition.pygame.settings import Settings


class AIButton(Button):
    
    #Constructor
    def __init__(self,
                 screen, 
                 settings:Settings,
                 ai:AI, 
                 width:int = 200, 
                 height:int = 50, 
                 button_color:() = (0, 0, 255), 
                 text_color:() = (255, 255, 255),
                 padding:int = 3):
        
        super().__init__(screen, settings, ai.get_name(), width, height, button_color, text_color, padding)
        
        #initialize fields
        self.__ai = ai
        self.__selected:bool = False
    
    #Setters and Getters
    def get_ai(self):
        return self.__ai
    def is_selected(self):
        return self.__selected
    def set_selected(self, selected:bool):
        if selected:
            self.set_button_color((82, 240, 108))
        else:
            self.set_button_color((0, 0, 255))
        self.__selected = selected
        self.prep_msg(self.get_text())
    
    #Other Methods
    