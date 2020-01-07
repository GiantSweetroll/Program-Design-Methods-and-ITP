import pygame

from final_project.handwritting_recognition import constants
from final_project.handwritting_recognition.pygame import game_functions, \
    globals
from final_project.handwritting_recognition.pygame.game_panels.draw_panel import DrawPanel


class DrawPanelGame(DrawPanel):
    
    #Constructor
    def __init__(self, screen, settings):
        super().__init__(screen, settings, "Draw a character for the AI to guess")
        
        self.get_exit_button().set_text("Back")
        self.get_exit_button().prep_msg(self.get_exit_button().get_text())
        
        self._draw_sub_title_label = True
    
    #Overridden Methods
    def check_exit_button(self, mouse_pos:()):
        """Goes back to previous panel"""
        if game_functions.mouse_on_button(self.get_exit_button(), mouse_pos):
            globals.panel_index -= 1
    
    def check_guess_button(self, mouse_pos:()):
        """Check for guess button presses"""
        if game_functions.mouse_on_button(self.get_guess_button(), mouse_pos):
            self.set_guess_button_pressed(True)
            #Remove the sub title label, exit, guess, and clear buttons to capture only the drawn image and then restore it
            self.get_buttons_to_draw().clear()
            self.set_draw_sub_title_label(False)
            self.draw_components()
            pygame.image.save(self.get_screen(), constants.pygame_image_path + constants.pygame_test_image_name)     #Take a screenshot of the game screen window and save it to disk
            self._buttons_to_draw = [self.get_exit_button(), self.get_guess_button(), self.get_clear_button()] #Add the buttons back
            self.set_draw_sub_title_label(True)   #Draw the sub title label again
            
            #Connect to loading screen
            globals.loading_active = True
            globals.panel_index += 1