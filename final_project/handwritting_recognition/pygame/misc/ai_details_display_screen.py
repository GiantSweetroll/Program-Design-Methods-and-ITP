import pygame
from pygame.rect import Rect

from final_project.handwritting_recognition.pygame.labels.label import Label


class AIDetailsDisplayScreen():
    
    #Constructor
    def __init__(self, width:int = 300, height:int = 600):
        self.__rect:Rect = Rect(0, 0, width, height)
        self.__background_color = (0, 0, 0, 100)
        self.__font = pygame.font.SysFont(None, 15)
        self.__background_color:() = (0, 0, 0, 100)
        self.__model_sum_label:Label = Label("", self.__font)
        self.__model_structure_labels:[] = []
        
        #Configure component placement
        model_sum_rect:Rect = self.__model_sum_label.get_rect()
        model_sum_rect.top = self.get_rect().top
#         model_sum_rect.centerx = self.get_rect().centerx
        model_sum_rect.left = self.get_rect().left
        
    #Setters and Getters
    def get_rect(self):
        return self.__rect
    def get_background_color(self) -> ():
        return self.__background_color
    def get_model_sum_label(self) -> Label:
        return self.__model_sum_label
    def set_background_color(self, color:()):
        """
        Set the background color
        color: RGB or RGBA tuple
        """
        self.__background_color = color
    def set_model_sum_text(self, model_sum:str):
        """
        Sets the display text of the AI model summary
        """
        self.__model_sum_label.set_text(model_sum, True)
    
    #Other Methods
    def draw(self, screen):
        screen.fill(self.get_background_color(), self.get_rect())
        self.get_model_sum_label().draw(screen)