from pygame.rect import Rect

from final_project.handwritting_recognition.pygame import game_functions,\
    globals
from final_project.handwritting_recognition.pygame.buttons.ai_button import AIButton
from final_project.handwritting_recognition.pygame.data_drivers.ai_random import RandomAI
from final_project.handwritting_recognition.pygame.game_panels.choose_ai_panel import ChooseAIPanel
from final_project.handwritting_recognition.pygame.settings import Settings


class RandomChooseAIPanel(ChooseAIPanel):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings)
    
    #Overridden Methods
    def init_ai_buttons(self):
        #Init
        ai_buttons:[AIButton] = self.get_ai_buttons()
        
        tot_height:int = 0
        for i in range(5):
            ai_buttons.append(AIButton(self.get_screen(), 
                                       self.get_settings(), 
                                       RandomAI(), 
                                       padding = 10))
            tot_height += ai_buttons[i].get_rect().height       #Add total height of the buttons
        
        #Placement configuration
        rect:Rect = Rect(0, 0, ai_buttons[0].get_rect().width, tot_height)
        rect.centery = self.get_screen().get_rect().centery
        rect.centerx = self.get_screen().get_rect().centerx//3
        #Configure first button
        padding:int = 5
        ai_buttons[0].get_rect().top = rect.top - padding
        ai_buttons[0].get_rect().left = rect.left
        ai_buttons[0].prep_msg(ai_buttons[0].get_text())
        #Configure remaining buttons
        for i in range(1, len(ai_buttons)):
            ai_buttons[i].get_rect().top = ai_buttons[i-1].get_rect().bottom + padding
            ai_buttons[i].get_rect().left = rect.left
            ai_buttons[i].prep_msg(ai_buttons[i].get_text())
    
    def check_back_button(self, mouse_pos:()):
        """Check if back button was pressed"""
        if game_functions.mouse_on_button(self.get_back_button(), mouse_pos):
            globals.panel_index = 0     #Go to main menu
    
    def check_choose_button(self, mouse_pos:()):
        """Method to check when the choose button is pressed"""
        if game_functions.mouse_on_button(self.get_choose_button(), mouse_pos) and self.get_choose_button().is_enabled():
            globals.active_ai = self.get_selected_button().get_ai()
            globals.panel_index += 1     #Go to draw panel