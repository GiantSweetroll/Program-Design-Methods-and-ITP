from pygame.event import Event

from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.settings import Settings
from final_project.handwritting_recognition.pygame import game_functions,\
    globals
import pygame


class InstructionsPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings, background_img_path="instructions.png")
        
        self.__ok_button:Button = Button(screen, settings, "Ok")
        
        #Component placement configuration
        screen_rect:Rect = screen.get_rect()
        #Ok Button
        self.__ok_button.get_rect().centery = screen_rect.bottom - self.__ok_button.get_height()
        self.__ok_button.prep_msg(self.__ok_button.get_text())
    
    #Other Methods
    def check_ok_button(self, mouse_pos:()):
        """Check if the ok button was clicked"""
        if game_functions.mouse_on_button(self.__ok_button, mouse_pos):
            globals.panel_index = 0 #Go to main menu
    
    #Overridden Methods
    def check_events(self, event:Event):
        x, y = game_functions.get_mouse_position()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       #1 is left mouse button
                self.check_ok_button((x, y))
    
    def draw_components(self):
        super().draw_components()
        
        self.__ok_button.draw()
        
        pygame.display.flip()

    def reset_defaults(self):
        super().reset_defaults()