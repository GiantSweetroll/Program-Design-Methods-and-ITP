import pygame
class Console():
    """Class to store an image as an object"""
    
    #Constructor
    def __init__(self, path=None, image = None):
        """
        Fill one of the following parameters:
        path: path of the image
        image: the image itself in pygame.image.load() format
        """
        self.__image_idle = pygame.image.load(path) if path != None else image if image != None else None
        self.__rect = self.__image_idle.get_rect() if self.__image_idle != None else None
    
    #Setters and Getters
    def set_image(self, path:str = None, image = None):
        """
        Fill one of the following parameters:
        path: path of the image
        image: the image itself in pygame.image.load() format
        """
        try:
            self.__image_idle = pygame.image.load(path) if path != None else image
            
            #Retain some of the original rect positions
            rect:Rect = self.__rect
            self.__rect = self.__image_idle.get_rect()
            if rect != None:
                self.__rect.center = rect.center
        except:
            pass
    def get_rect(self):
        return self.__rect
    def get_image_idle(self):
        return self.__image_idle
    
    #Other methods
    def draw(self, screen):
        """
        Method to draw the image to the screen
        
        screen: the pygame screen
        """
        screen.blit(self.__image_idle, self.get_rect())