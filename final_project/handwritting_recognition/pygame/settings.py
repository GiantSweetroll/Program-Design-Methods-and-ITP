import pygame

from final_project.handwritting_recognition.pygame.data_drivers.ai import AI


class Settings():

    #Constructor
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 760
        self.background_color = (35, 34, 90)
        self.pen_color = (0, 0, 0)
        self.pen_size = 40
        self.button_text_font = pygame.font.SysFont(None, 48)
        self.sub_title_font = pygame.font.SysFont(None, 56)
        
        #Initialize AI actors
        self.ai_list:[AI] = [AI]
        