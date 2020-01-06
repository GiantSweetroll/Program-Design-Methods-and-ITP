import os

import pygame

from final_project.handwritting_recognition import constants
from final_project.handwritting_recognition.pygame.data_drivers.ai import AI
import random


class RandomAI(AI):
    
    #Constructor
    def __init__(self):
        #Randomize AI Folder
        root_folder:str = "ai_files"
        folders = [folder for folder in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, folder))]
        super().__init__("??????????", root_folder + "/" + random.choice(folders) + "/")
        
        self._image_idle_path = constants.path_img_mystery_ai
        self._image_processing_path = constants.path_img_mystery_ai
        self._image_idle = pygame.image.load(self._image_idle_path)
        self._image_processing = pygame.image.load(self._image_processing_path)
        self._image_info_screen_path = constants.path_img_ai_info_empty
    
    #Other Methods
    def get_nicer_name(self):
        return "AI"