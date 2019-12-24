import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    #Constructor
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        #Load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact position
        self.x = float(self.rect.x)
    
    #Methods
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.x += self.settings.alienSpeedFactor * self.settings.fleetDirection
        self.rect.x = self.x
    def checkEdges(self):
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= 0:
            return True