import pygame
from pygame.event import Event

from final_project.handwritting_recognition import constants
from final_project.handwritting_recognition.pygame import game_functions as gf,\
    globals
from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
from final_project.handwritting_recognition.pygame.misc.console import Console
from final_project.handwritting_recognition.pygame.settings import Settings


class GamemodePanel(Panel):
    """A class that holds the gamemode selection panel"""
    #Constructor
    def __init__(self, screen, settings:Settings):
        """
        screen: the pygame screen
        settings: the Settings object
        """
        super().__init__(screen, settings)
        
        #Initialize fields
        padding:int = 20
        self.__console:Console = Console(constants.path_img_gamemode_welc_console)
        self.__funhouse_button:Button = Button(screen, settings, "Fun House", width = (settings.screen_width//2)-padding*2)
        self.__random_chaos_button:Button = Button(screen, settings, "Random Chaos", width = (settings.screen_width//2)-padding*2)
        self.__back_button:Button = Button(screen, settings, "Back", button_color=constants.color_red)
        self.__sub_title_font = settings.sub_title_font
        self._sub_title_label = Label("Select Game Mode", 
                                       font = self.__sub_title_font, 
                                       bold=True,
                                       width = settings.screen_width)
        
        #Configure component placements
        screen_rect:Rect = self.get_screen().get_rect()
        #Funhouse button
        self.get_funhouse_button().get_rect().centerx = screen_rect.centerx//2
        self.get_funhouse_button().get_rect().centery = 4*screen_rect.centery//5       
        self.get_funhouse_button().prep_msg(self.get_funhouse_button().get_text())
        #Random chaos button
        self.get_random_chaos_button().get_rect().centerx = screen_rect.centerx//2
        self.get_random_chaos_button().prep_msg(self.get_random_chaos_button().get_text())
        #Back Button
        self.get_back_button().get_rect().centerx = screen_rect.centerx//2
        self.get_back_button().get_rect().centery = screen_rect.centery + screen_rect.centery//2
        self.get_back_button().prep_msg(self.get_back_button().get_text())
        #Sub title text
        self.get_sub_title_label().get_rect().top = screen_rect.top + 20
#         txt_width, _ = self.get_sub_title_label().get_font().size(self.get_sub_title_label().get_text())
#         self.get_sub_title_label().get_rect().left = screen_rect.centerx - txt_width//2 #Fake center of text
        self.get_sub_title_label().get_rect().centerx = screen_rect.centerx
        #Console image
        console_rect = self.get_console().get_rect()
        console_rect.centerx = screen_rect.centerx + screen_rect.centerx//2
        console_rect.centery = screen_rect.centery
        
    #Setters and Getters
    def get_funhouse_button(self) -> Button:
        return self.__funhouse_button
    def get_random_chaos_button(self) -> Button:
        return self.__random_chaos_button
    def get_back_button(self) -> Button:
        return self.__back_button
    def get_sub_title_font(self):
        return self.__sub_title_font
    def get_sub_title_label(self):
        return self._sub_title_label
    def get_console(self) -> Console:
        """Method to get the console class object"""
        return self.__console
    
    #Other Methods
    def check_funhouse_button(self, mouse_pos:()):
        if gf.mouse_on_button(self.get_funhouse_button(), mouse_pos):
            globals.panel_index+=1
    def check_random_chaos_button(self, mouse_pos:()):
        if gf.mouse_on_button(self.get_random_chaos_button(), mouse_pos):
            #TO-DO
            pass
    def check_back_button(self, mouse_pos:()):
        """Back button action"""
        if gf.mouse_on_button(self.get_back_button(), mouse_pos):
            #Go back to previous page
            globals.panel_index-=1
    
    #Overridden Methods
    def check_events(self, event:Event):
        super().check_events(event)
        x, y = gf.get_mouse_position()
        
        #Check for mouse hovers
        if gf.mouse_on_button(self.get_funhouse_button(), (x, y)):
            self.get_console().set_image(constants.path_img_gamemode_funhouse_console)
        elif gf.mouse_on_button(self.get_random_chaos_button(), (x, y)):
            self.get_console().set_image(constants.path_img_gamemode_random_chaos_console)
        else:
            self.get_console().set_image(constants.path_img_gamemode_welc_console)
        
        #Check for mouse presses
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #1 is left click
                self.check_funhouse_button((x, y))
                self.check_random_chaos_button((x, y))
                self.check_back_button((x, y))
    def draw_components(self):
        super().draw_components()
        
        self.get_sub_title_label().draw(self.get_screen())
        self.get_funhouse_button().draw_button()
        self.get_random_chaos_button().draw_button()
        self.get_back_button().draw_button()
        self.get_console().draw(self.get_screen())
        
        pygame.display.flip()