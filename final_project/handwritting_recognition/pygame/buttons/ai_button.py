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
                 button_color:() = (23, 74, 211, 220), 
                 text_color:() = (255, 255, 255),
                 padding:int = 3):
        
        super().__init__(screen, settings, ai.get_name(), width=width, height=height, button_color=button_color, text_color=text_color, padding=padding)
        
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
            self.set_button_color(self.settings.button_color_selected)
        else:
            self.set_button_color(self.settings.button_color_general)
        self.__selected = selected
        self.prep_screen()
