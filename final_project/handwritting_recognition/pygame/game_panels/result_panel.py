from pygame.event import Event

from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
from final_project.handwritting_recognition.pygame.misc.console import Console
from final_project.handwritting_recognition.pygame.settings import Settings
import pygame
from final_project.handwritting_recognition.pygame import globals,\
    game_functions
from final_project.handwritting_recognition import constants


class ResultPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings)
        
        #Initialize components
        self.__sub_title_label:Label = Label()
        self.__ori_image:Console = Console()
        self.__is_label:Label = Label("is", bold=False)
        self.__guess_label:Label = Label(font_size=250)
        self.__finish_button:Button = Button(screen, settings, "Finish")
        self.__prepared:bool = False
            
        #Configure component positioning
        screen_rect:Rect = screen.get_rect()
        #Is Label
        self.__is_label.get_rect().center = screen_rect.center
        #Finish button
        self.__finish_button.get_rect().right = screen_rect.right - 20
        self.__finish_button.get_rect().centery = screen_rect.bottom - self.__finish_button.get_height()
        self.__finish_button.prep_msg(self.__finish_button.get_text())
    
    #Other Methods
    def __prepare(self):
        """Method to prepare the components for display"""
        self.__sub_title_label.set_text(globals.active_ai.get_name() + " guessed...", True)
        self.__ori_image.set_image(image = pygame.transform.scale(pygame.image.load(constants.pygame_image_path + constants.pygame_test_image_name), (313, 313)))
        self.__guess_label.set_text(globals.prediction, True)
        
        #Configure placements
        #Sub title
        self.__sub_title_label.get_rect().top = self.get_screen().get_rect().top + 20
        self.__sub_title_label.get_rect().centerx = self.get_screen().get_rect().centerx
        #Ori image
#         self.__ori_image.get_rect().right = self.__is_label.get_rect().left - 50
        self.__ori_image.get_rect().centerx = self.get_screen().get_rect().centerx//2
        self.__ori_image.get_rect().centery = self.__is_label.get_rect().centery
        #AI Guess label
        self.__guess_label.get_rect().centerx = self.get_screen().get_rect().centerx + self.get_screen().get_rect().centerx//2
        self.__guess_label.get_rect().centery = self.__is_label.get_rect().centery
        
        self.__prepared = True
    
    def check_finish_button(self, mouse_pos:()):
        """Method to check if the finish button is pressed"""
        if game_functions.mouse_on_button(self.__finish_button, mouse_pos):
            #Move to main menu screen
            globals.panel_index = 0
            globals.reset_defaults = True
    
    #Overridden Methods
    def check_events(self, event:Event):
        super().check_events(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   #1 is left mouse click
                x, y = game_functions.get_mouse_position()
                self.check_finish_button((x, y))
    
    def draw_components(self):
        super().draw_components()
        
        if globals.show_results:
            if not self.__prepared:
                self.__prepare()
            
            #Draw components
            self.__sub_title_label.draw(self.get_screen())
            self.__ori_image.draw(self.get_screen())
            self.__is_label.draw(self.get_screen())
            self.__guess_label.draw(self.get_screen())
            self.__finish_button.draw_button()
        
        pygame.display.flip()
    
    def reset_defaults(self):
        super().reset_defaults()
        
        self.__init__(self.get_screen(), self.get_settings())