import pygame
from pygame.event import Event

from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.buttons.exit_button import ExitButton
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.settings import Settings


class MainMenuPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings)
        
        #Fields initialization
        self.__start_button = Button(screen, settings, "Start")
        self.__instructions_button = Button(screen, settings, "Instructions")
        self.__exit_button = ExitButton(screen, settings)
        
        #Configure Buttons
        self.get_start_button().width = 3*self.get_settings().screen_width//5
        self.get_instructions_button().width = 3*self.get_settings().screen_width//5
        
        #Configure button placements
        padding:int = 10
        screen_rect:Rect = self.get_screen().get_rect()
        #Start button
        self.get_start_button().get_rect().left = screen_rect.left + settings.screen_width//5
        self.get_start_button().get_rect().right = screen_rect.right - settings.screen_width//5
        self.get_start_button().get_rect().centery = screen_rect.centery - self.get_start_button().height//2 - padding//5
        self.get_start_button().prep_msg(self.get_start_button().get_text())
        #Instructions button 
        self.get_instructions_button().get_rect().left = screen_rect.left + settings.screen_width//5
        self.get_instructions_button().get_rect().right = screen_rect.right - settings.screen_width//5
        self.get_instructions_button().get_rect().centery = screen_rect.centery + self.get_instructions_button().height//2 + padding//5
        self.get_instructions_button().prep_msg(self.get_instructions_button().get_text())
        #Exit button
        self.get_exit_button().get_rect().left = screen_rect.left + settings.screen_width//5
        self.get_exit_button().get_rect().right = screen_rect.right - settings.screen_width//5
        self.get_exit_button().get_rect().top = self.get_instructions_button().get_rect().bottom + padding*2
        self.get_exit_button().prep_msg(self.get_exit_button().get_text())
    
    #Setters and Getters
    def get_start_button(self) -> Button:
        return self.__start_button
    def get_instructions_button(self) -> Button:
        return self.__instructions_button
    def get_exit_button(self) -> ExitButton:
        return self.__exit_button
    
    #Overridden Methods
    def check_events(self, event:Event):
        super().check_events(event)
    def draw_components(self):
        super().draw_components()
        
        #Draw buttons
        self.get_start_button().draw_button()
        self.get_instructions_button().draw_button()
        self.get_exit_button().draw_button()
        
        pygame.display.flip()