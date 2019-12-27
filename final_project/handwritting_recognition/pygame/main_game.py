import pygame

import final_project.handwritting_recognition.pygame.game_functions as gf
from final_project.handwritting_recognition.pygame.gui_objects.clear_button import ClearButton
from final_project.handwritting_recognition.pygame.gui_objects.exit_button import ExitButton
from final_project.handwritting_recognition.pygame.gui_objects.guess_button import GuessButton
from final_project.handwritting_recognition.pygame.settings import Settings
from final_project.handwritting_recognition.pygame import globals
from final_project.handwritting_recognition.neural_network import NeuralNetwork

class MainGame():
    
    #Constructor
    def __init__(self, neural_network:NeuralNetwork):
        self.run_game(neural_network)
        
    #Methods
    def run_game(self, neural_network:NeuralNetwork):
        pygame.init()
        settings = Settings()
        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Guess the Letter")
        
        exit_button = ExitButton(screen)
        guess_button = GuessButton(screen)
        clear_button = ClearButton(screen)
        globals.buttons_to_draw = [exit_button, guess_button, clear_button]
        
        #While game runs
        while True:
            gf.check_events(neural_network, screen, settings, exit_button, guess_button, clear_button)
            
            gf.update_screen(screen, settings, globals.buttons_to_draw)