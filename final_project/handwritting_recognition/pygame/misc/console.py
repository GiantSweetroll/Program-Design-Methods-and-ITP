import pygame
class Console():
    
    #Constructor
    def __init__(self, path):
        self.path = path
        self.__image_idle = pygame.image.load(path)
        self.__rect = self.__image_idle.get_rect()
    
    #Setters and Getters
    def set_image(self, path:str):
        try:
            self.__image_idle = pygame.image.load(path)
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