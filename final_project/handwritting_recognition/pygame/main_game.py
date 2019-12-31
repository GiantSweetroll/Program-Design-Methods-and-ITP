import pygame

from final_project.handwritting_recognition.neural_network import NeuralNetwork
import final_project.handwritting_recognition.pygame.game_functions as gf
from final_project.handwritting_recognition.pygame.game_panels.draw_panel import DrawPanel
from final_project.handwritting_recognition.pygame.settings import Settings
from final_project.handwritting_recognition.pygame import game_functions
from final_project.handwritting_recognition.pygame.game_panels.main_menu_panel import MainMenuPanel
from final_project.handwritting_recognition.pygame.game_panels.gamemode_panel import GamemodePanel


class MainGame():
    
    #Constructor
    def __init__(self):
        self.run_game()
        
    #Methods
    def run_game(self):
        pygame.init()
        settings = Settings()
        screen = game_functions.create_screen(settings)
        pygame.display.set_caption("AI Roulette")
        
        #Panel initialization
#         draw_panel:Panel = DrawPanel(screen, settings)
#         draw_panel.set_neural_network(neural_network)
        main_menu_panel:Panel = MainMenuPanel(screen, settings)
        gamemode_panel:Panel = GamemodePanel(screen, settings)
        
        #While game runs
        while True:
            gf.check_events(gamemode_panel)
            gf.update_screen(screen, settings, gamemode_panel)