from final_project.handwritting_recognition.pygame import game_functions, \
    globals
from final_project.handwritting_recognition.pygame.game_panels.draw_panel.draw_panel_game import DrawPanelGame
from final_project.handwritting_recognition.pygame.settings import Settings


class DrawPanelGameRandom(DrawPanelGame):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings)
    
    #Overridden Methods
    def check_guess_button(self, mouse_pos:()):
        """Go to loading screen"""
        globals.panel_index = 3
        super().check_guess_button(mouse_pos)
        globals.active_ai.set_name("AI")
    
    def check_exit_button(self, mouse_pos:()):
        """Go to previous panel"""
        if game_functions.mouse_on_button(self.get_exit_button(), mouse_pos):
            globals.panel_index -= 1