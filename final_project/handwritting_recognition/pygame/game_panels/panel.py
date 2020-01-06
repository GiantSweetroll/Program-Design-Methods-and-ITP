from abc import abstractclassmethod

from pygame.event import Event

from final_project.handwritting_recognition.pygame.settings import Settings


class Panel():
    
    #Constructors
    def __init__(self, screen, settings:Settings):
        self._screen = screen
        self._settings:Settings = settings
        
    #Setters and Getters
    def get_screen(self):
        return self._screen
    def set_screen(self, screen):
        self._screen = screen
    def get_settings(self) -> Settings:
        return self._settings
    def set_settings(self, settings:Settings):
        self._settings = settings
    
    #Abstract Methods
    @abstractclassmethod
    def check_events(self, event:Event):
        """Abstract method to check for events"""
        pass
    
    @abstractclassmethod
    def draw_components(self):
        """Abstract method to draw the components of the screen"""
        pass
    
    @abstractclassmethod
    def reset_defaults(self):
        """Reset the components to their default states"""
        pass