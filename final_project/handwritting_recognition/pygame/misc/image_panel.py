import pygame

class ImagePanel():
    """Class to store an image as an object"""
    
    #Constructor
    def __init__(self, path=None, image = None):
        """
        Fill one of the following parameters:
        path: path of the image
        image: the image itself in pygame.image.load() format
        """
        self.image = pygame.image.load(path) if path != None else image if image != None else None
        self.__rect = self.image.get_rect() if self.image != None else None
    
    #Setters and Getters
    def set_image(self, path:str = None, image = None):
        """
        Fill one of the following parameters:
        path: path of the image
        image: the image itself in pygame.image.load() format
        """
        try:
            self.image = pygame.image.load(path) if path != None else image
            
            #Retain some of the original rect positions
            rect:Rect = self.__rect
            self.__rect = self.image.get_rect()
            if rect != None:
                self.__rect.center = rect.center
        except:
            pass
        
    def get_rect(self):
        return self.__rect
    
    def get_image(self):
        return self.image
    
    #Other methods
    def draw(self, screen):
        """
        Method to draw the image to the screen
        
        screen: the pygame screen
        """
        screen.blit(self.image, self.get_rect())