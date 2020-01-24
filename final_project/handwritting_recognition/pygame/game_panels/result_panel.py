import pygame
from pygame.event import Event
from pygame.rect import Rect

from final_project.handwritting_recognition import constants
from final_project.handwritting_recognition.pygame import globals, \
    game_functions
from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.data_drivers.ai import AI
from final_project.handwritting_recognition.pygame.data_drivers.ai_random import RandomAI
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
from final_project.handwritting_recognition.pygame.misc.image_panel import ImagePanel
from final_project.handwritting_recognition.pygame.settings import Settings


class ResultPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings, background_img_path="monitor.png")
        
        #Initialize components
        self.__sub_title_label:Button = Button(screen, settings, "", button_color = None)
        self.__ori_image:ImagePanel = ImagePanel()
        self.__is_label:Button = Button(screen, settings, "is", button_color = None)
        self.__guess_label:Button = Button(screen, settings, "", button_color = None, font=settings.large_font)
        self.__finish_button:Button = Button(screen, settings, "Finish")
        self.__prepared:bool = False
        self.__punishment_labels:[] = []
        
        #Initialize the punishment labels
        self.__punishment_labels.append(Button(screen, settings, "Was the guess correct?", button_color = None))
        self.__punishment_labels.append(Button(screen, settings, "If not, give punishment to the player. Otherwise, give", button_color = None, padding=1))
        self.__punishment_labels.append(Button(screen, settings, "punishment to everyone else. Punishment can be truth or", button_color = None, padding=1))
        self.__punishment_labels.append(Button(screen, settings, "dare, push-ups, sing, etc.", button_color = None, padding=1))
         
        #Configure component positioning
        screen_rect:Rect = screen.get_rect()
        #Finish button
        self.__finish_button.get_rect().right = screen_rect.right - 20
        self.__finish_button.get_rect().centery = screen_rect.bottom - self.__finish_button.get_height()
        self.__finish_button.prep_msg(self.__finish_button.get_text())
            
    #Other Methods
    def __prepare(self):
        """Method to prepare the components for display"""
        self.__ori_image.set_image(image = pygame.transform.scale(pygame.image.load(constants.pygame_image_path + constants.pygame_test_image_name), (313, 313)))
        self.__guess_label.set_text(globals.prediction)
        
        #Play sound effect
        pygame.mixer.music.load("audio/finished.mp3")
        pygame.mixer.music.play()
        
        #Configure placements
        #Sub title
        self.__sub_title_label.get_rect().top = self.get_screen().get_rect().top + 30
        self.__sub_title_label.get_rect().centerx = self.get_screen().get_rect().centerx
        self.__sub_title_label.set_text(globals.active_ai.get_name() + " guessed..." if isinstance(globals.active_ai, AI) else globals.active_ai.get_nicer_name() + " guessed...")
        #Ori image
#         self.__ori_image.get_rect().right = self.__is_label.get_rect().left - 50
        self.__ori_image.get_rect().centerx = self.get_screen().get_rect().centerx//2
        self.__ori_image.get_rect().centery = 2*self.get_screen().get_rect().centery//3
        #Is Label
        self.__is_label.get_rect().centery = self.__ori_image.get_rect().centery
        self.__is_label.get_rect().centerx = self.get_screen().get_rect().centerx
        self.__is_label.prep_msg(self.__is_label.get_text())
        #AI Guess label
        self.__guess_label.get_rect().centerx = self.get_screen().get_rect().centerx + self.get_screen().get_rect().centerx//2
        self.__guess_label.get_rect().centery = self.__is_label.get_rect().centery
        self.__guess_label.prep_msg(self.__guess_label.get_text())
        #Punishment labels
        max_width:int = 0
        for label in self.__punishment_labels:
            width = label.get_rect().width
            if width > max_width:
                max_width = width
        rect:Rect = Rect(0, 0, max_width, 1)
        rect.top = self.__ori_image.get_rect().bottom + 20
        rect.left = self.get_screen().get_rect().left + 50
        self.__punishment_labels[0].get_rect().left = rect.left
        self.__punishment_labels[0].get_rect().top = rect.top
        self.__punishment_labels[0].prep_msg(self.__punishment_labels[0].get_text())
        for a in range(1, len(self.__punishment_labels)):
            self.__punishment_labels[a].get_rect().top = self.__punishment_labels[a-1].get_rect().bottom
            self.__punishment_labels[a].get_rect().left = self.__punishment_labels[a-1].get_rect().left
            self.__punishment_labels[a].prep_msg(self.__punishment_labels[a].get_text())
        
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
            self.__sub_title_label.draw()
            self.__ori_image.draw(self.get_screen())
            self.__is_label.draw()
            self.__guess_label.draw()
            self.__finish_button.draw()
            for label in self.__punishment_labels:
                label.draw()
        
        pygame.display.flip()
    
    def reset_defaults(self):
        super().reset_defaults()
        
        self.__init__(self.get_screen(), self.get_settings())