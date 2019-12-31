import pygame

from final_project.handwritting_recognition.pygame import game_functions as gf
from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
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
        self.__funhouse_button:Button = Button(screen, settings, "Fun House")
        self.__random_chaos_button:Button = Button(screen, settings, "Random Chaos")
        self.__sub_title_font = settings.sub_title_font
        self.__sub_title_label = Label("Select Game Mode", 
                                       font = self.__sub_title_font, 
                                       bold=True,
                                       background_color=(255, 122, 233),
                                       width = settings.screen_width)
        
        #Configure button placements
        screen_rect:Rect = self.get_screen().get_rect()
        #Sub title text
        self.get_sub_title_label().get_rect().centerx = screen_rect.centerx
    
    #Setters and Getters
    def get_funhouse_button(self):
        return self.__funhouse_button
    def get_random_chaos_button(self):
        return self.__random_chaos_button
    def get_sub_title_font(self):
        return self.__sub_title_font
    def get_sub_title_label(self):
        return self.__sub_title_label
    
    #Other Methods
    def check_funhouse_button(self, mouse_pos:()):
        if gf.button_clicked(self.get_funhouse_button(), mouse_pos):
            #TO-DO
            pass
    def check_random_chaos_button(self, mouse_pos:()):
        if gf.button_clicked(self.get_random_chaos_button(), mouse_pos):
            #TO-DO
            pass
    
    #Overridden Methods
    def check_events(self, event):
        super().check_events(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.mouse == 1: #1 is left click
                x, y = gf.get_mouse_position()
                self.check_funhouse_button((x, y))
                self.check_random_chaos_button((x, y))
    def draw_components(self):
        super().draw_components()
        
        self.get_sub_title_label().draw(self.get_screen())
        
        pygame.display.flip()