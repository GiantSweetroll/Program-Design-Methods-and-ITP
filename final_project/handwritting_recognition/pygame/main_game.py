import pygame

from final_project.handwritting_recognition.pygame import globals
import final_project.handwritting_recognition.pygame.game_functions as gf
from final_project.handwritting_recognition.pygame.game_panels.choose_ai.choose_ai_panel import ChooseAIPanel
from final_project.handwritting_recognition.pygame.game_panels.choose_ai.random_choose_ai_panel import RandomChooseAIPanel
from final_project.handwritting_recognition.pygame.game_panels.draw_panel.draw_panel_game import DrawPanelGame
from final_project.handwritting_recognition.pygame.game_panels.draw_panel.draw_panel_game_random import DrawPanelGameRandom
from final_project.handwritting_recognition.pygame.game_panels.gamemode_panel import GamemodePanel
from final_project.handwritting_recognition.pygame.game_panels.loading_screen import LoadingScreen
from final_project.handwritting_recognition.pygame.game_panels.main_menu_panel import MainMenuPanel
from final_project.handwritting_recognition.pygame.game_panels.result_panel import ResultPanel
from final_project.handwritting_recognition.pygame.settings import Settings
from final_project.handwritting_recognition.pygame.game_panels.instructions_panel import InstructionsPanel


class MainGame():
    
    #Constructor
    def __init__(self):
        
        #Initialize fields
        pygame.init()
        self.__settings = Settings()
        self.__screen = gf.create_screen(self.__settings)
        pygame.display.set_caption("AI Roulette")
        self.__panels:[Panel] = []

        self.__main_menu_panel:MainMenuPanel = MainMenuPanel(self.__screen, self.__settings)
        self.__gamemode_panel:GamemodePanel = GamemodePanel(self.__screen, self.__settings)
        self.__ai_selection_panel:ChooseAIPanel = ChooseAIPanel(self.__screen, self.__settings)
        self.__draw_panel_game_panel:DrawPanelGame = DrawPanelGame(self.__screen, self.__settings)
        self.__loading_screen:LoadingScreen = LoadingScreen(self.__screen, self.__settings)
        self.__result_panel:ResultPanel = ResultPanel(self.__screen, self.__settings)
        self.__random_ai_selection_panel:RandomChooseAIPanel = RandomChooseAIPanel(self.__screen, self.__settings)
        self.__draw_panel_game_random_panel:DrawPanelGameRandom = DrawPanelGameRandom(self.__screen, self.__settings)
        self.__instructions_panel:InstructionsPanel = InstructionsPanel(self.__screen, self.__settings)
        
#         draw_panel:Panel = DrawPanel(self.__screen, self.__settings)
#         draw_panel.set_neural_network(neural_network)
        
        #Add to panel list
        self.__panels.append(self.__main_menu_panel)
        self.__panels.append(self.__gamemode_panel)
        self.__panels.append(self.__ai_selection_panel)
        self.__panels.append(self.__draw_panel_game_panel)
        self.__panels.append(self.__loading_screen)
        self.__panels.append(self.__result_panel)
        self.__panels.append(self.__random_ai_selection_panel)
        self.__panels.append(self.__draw_panel_game_random_panel)
        self.__panels.append(self.__instructions_panel)
#         self.__panels.append(draw_panel)
        
    #Methods
    def reset_defaults(self):
        """Method to reset defaults of the game components"""
        #Reset panels
        for panel in self.__panels:
            panel.reset_defaults()
        
        #Reset global variables
        globals.mouse_left_pressed = False
        globals.active_ai = None
        globals.loading_active = False
        globals.show_results = False
        globals.loading_progress = ""
        
        globals.reset_defaults = False  #turn off identifier
        
    def run_game(self):
        """Method to run the game"""
        #While game runs
        while True:
            gf.check_events(self.__panels[globals.panel_index])
            gf.update_screen(self.__screen, self.__settings, self.__panels[globals.panel_index])
            
            #Check for reset ping
            if globals.reset_defaults:
                self.reset_defaults()