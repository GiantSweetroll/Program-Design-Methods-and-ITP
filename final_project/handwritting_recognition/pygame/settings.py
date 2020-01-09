import pygame

from final_project.handwritting_recognition.pygame.data_drivers.ai import AI


class Settings():

    #Constructor
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 760
        self.background_color = (255, 255, 255) #(183, 195, 202)
        self.button_color_general = (23, 74, 211, 220)
        self.button_color_red = (237, 59, 59, 220)
        self.button_color_selected = (82, 240, 108, 220)
        self.button_color_disabled = (125, 125, 125, 220)
        self.pen_color = (0, 0, 0)
        self.pen_size = 40
        self.button_text_font = pygame.font.SysFont(None, 48)
        self.sub_title_font = pygame.font.SysFont(None, 56)
        self.super_large_font = pygame.font.SysFont(None, 500)
        self.large_font = pygame.font.SysFont(None, 250)
        self.title_font = pygame.font.SysFont("kristenitc", 72, 0)
        
        #Initialize AI actors
        self.ai_list:[AI] = [AI]
        