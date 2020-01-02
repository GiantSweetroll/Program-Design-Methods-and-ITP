import sys

import pygame
from pygame.event import Event

from final_project.handwritting_recognition.pygame import game_functions as gf,\
    globals
from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.settings import Settings
from final_project.handwritting_recognition import constants


class MainMenuPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        """
        screen: the pygame screen
        settings: the Settings object
        """
        super().__init__(screen, settings)
        
        #Fields initialization
        self.__start_button = Button(screen, settings, "Start")
        self.__instructions_button = Button(screen, settings, "Instructions")
        self.__exit_button = Button(screen, settings, "Exit", button_color=constants.color_red)
        
        #Configure Buttons
        self.get_start_button().set_width(3*self.get_settings().screen_width//5)
        self.get_instructions_button().set_width(3*self.get_settings().screen_width//5)
        
        #Configure button placements
        padding:int = 10
        screen_rect:Rect = self.get_screen().get_rect()
        #Start button
        self.get_start_button().get_rect().left = screen_rect.left + settings.screen_width//5
        self.get_start_button().get_rect().right = screen_rect.right - settings.screen_width//5
        self.get_start_button().get_rect().centery = screen_rect.centery - self.get_start_button().get_height()//2 - padding
        self.get_start_button().get_rect().centerx = self.get_screen().get_rect().centerx
        self.get_start_button().prep_msg(self.get_start_button().get_text())
        #Instructions button 
        self.get_instructions_button().get_rect().left = screen_rect.left + settings.screen_width//5
        self.get_instructions_button().get_rect().right = screen_rect.right - settings.screen_width//5
        self.get_instructions_button().get_rect().centery = screen_rect.centery + self.get_instructions_button().get_height()//2 + padding
        self.get_instructions_button().get_rect().centerx = self.get_screen().get_rect().centerx
        self.get_instructions_button().prep_msg(self.get_instructions_button().get_text())
        #Exit button
        self.get_exit_button().get_rect().left = screen_rect.left + settings.screen_width//5
        self.get_exit_button().get_rect().right = screen_rect.right - settings.screen_width//5
        self.get_exit_button().get_rect().top = self.get_instructions_button().get_rect().bottom + padding*2
        self.get_exit_button().get_rect().centerx = self.get_screen().get_rect().centerx
        self.get_exit_button().prep_msg(self.get_exit_button().get_text())
    
    #Setters and Getters
    def get_start_button(self) -> Button:
        return self.__start_button
    def get_instructions_button(self) -> Button:
        return self.__instructions_button
    def get_exit_button(self) -> Button:
        return self.__exit_button
    
    #Other Methods
    def check_exit_button(self, mouse_pos:()):
        """If exit button is pressed, exit the game"""
        if gf.mouse_on_button(self.get_exit_button(), mouse_pos):
            sys.exit()
    def check_start_button(self, mouse_pos:()):
        """Method to check if the start button was pressed"""
        if gf.mouse_on_button(self.get_start_button(), mouse_pos):
            #TO-DO start the game
            globals.panel_index+=1
            pass
    def check_instructions_button(self, mouse_pos:()):
        """Method to check if the instructions button was pressed"""
        if gf.mouse_on_button(self.get_instructions_button(), mouse_pos):
            #TO-DO open instructions
            pass
    
    #Overridden Methods
    def check_events(self, event:Event):
        super().check_events(event)
        
        #Check mouse button press events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       #1 is left mouse click
                x, y = gf.get_mouse_position()
                self.check_exit_button((x, y))
                self.check_instructions_button((x, y))
                self.check_start_button((x, y))
    def draw_components(self):
        super().draw_components()
        
        #Draw buttons
        self.get_start_button().draw_button()
        self.get_instructions_button().draw_button()
        self.get_exit_button().draw_button()
        
        pygame.display.flip()