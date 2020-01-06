import pygame

import final_project.handwritting_recognition.pygame.game_functions as gf
from final_project.handwritting_recognition.pygame.settings import Settings
from final_project.handwritting_recognition.pygame import game_functions,\
    globals
from final_project.handwritting_recognition.pygame.game_panels.main_menu_panel import MainMenuPanel
from final_project.handwritting_recognition.pygame.game_panels.gamemode_panel import GamemodePanel
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.game_panels.choose_ai_panel import ChooseAIPanel
from final_project.handwritting_recognition.pygame.game_panels.draw_panel_game import DrawPanelGame
from final_project.handwritting_recognition.pygame.game_panels.loading_screen import LoadingScreen
from final_project.handwritting_recognition.pygame.game_panels.result_panel import ResultPanel


class MainGame():
    
    #Constructor
    def __init__(self):
        
        #Initialize fields
        pygame.init()
        settings = Settings()
        screen = game_functions.create_screen(settings)
        pygame.display.set_caption("AI Roulette")
        self.__panels:[Panel] = []
#         draw_panel:Panel = DrawPanel(screen, settings)
#         draw_panel.set_neural_network(neural_network)
        main_menu_panel:MainMenuPanel = MainMenuPanel(screen, settings)
        gamemode_panel:GamemodePanel = GamemodePanel(screen, settings)
        ai_selection_panel:ChooseAIPanel = ChooseAIPanel(screen, settings)
        draw_panel_game_panel:DrawPanelGame = DrawPanelGame(screen, settings)
        loading_screen:LoadingScreen = LoadingScreen(screen, settings)
        result_panel:ResultPanel = ResultPanel(screen, settings)
        
        #Add to panel list
        self.__panels.append(main_menu_panel)
        self.__panels.append(gamemode_panel)
        self.__panels.append(ai_selection_panel)
        self.__panels.append(draw_panel_game_panel)
        self.__panels.append(loading_screen)
        self.__panels.append(result_panel)
        
        self.run_game(screen, settings)
        
    #Methods
    def run_game(self, screen, settings:Settings):
        #While game runs
        while True:
            gf.check_events(self.__panels[globals.panel_index])
            gf.update_screen(screen, settings, self.__panels[globals.panel_index])