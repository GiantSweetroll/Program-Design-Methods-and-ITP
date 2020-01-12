from abc import abstractclassmethod

from pygame.event import Event

from final_project.handwritting_recognition import constants
from final_project.handwritting_recognition.pygame.misc.image_panel import ImagePanel
from final_project.handwritting_recognition.pygame.settings import Settings


class Panel():
    
    #Constructors
    def __init__(self, screen, settings:Settings, background_img_path:str = None):
        """
        screen: the pygame screen
        settings: the Settings object
        background_img_path: path to the background image (just file name with extension)
        """
        self._screen = screen
        self._settings:Settings = settings
        self._background_img:ImagePanel = ImagePanel(path=constants.path_img_background_folder + background_img_path) if background_img_path != None else None
        
    #Setters and Getters
    def get_screen(self):
        return self._screen
    
    def set_screen(self, screen):
        self._screen = screen
        
    def get_settings(self) -> Settings:
        return self._settings
    
    def set_settings(self, settings:Settings):
        self._settings = settings
        
    #Other Methods
    def draw_components(self):
        """Method to draw the components of the screen"""
        if (self._background_img != None):
            self._background_img.draw(self._screen)
    
    #Abstract Methods
    @abstractclassmethod
    def check_events(self, event:Event):
        """Abstract method to check for events"""
        pass
    
    @abstractclassmethod
    def reset_defaults(self):
        """Reset the components to their default states"""
        pass