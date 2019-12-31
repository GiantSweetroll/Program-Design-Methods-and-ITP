import pygame

class Settings():

    #Constructor
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 760
        self.background_color = (255, 255, 255)
        self.pen_color = (0, 0, 0)
        self.pen_size = 10
        self.button_text_font = pygame.font.SysFont(None, 48)
        self.sub_title_font = pygame.font.SysFont(None, 56)