import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
        
    #Constructor
    def __init__(self, settings, screen):
        
        super().__init__()
        
        self.screen = screen
        self.settings = settings
        
        #Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()
        
        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
        
        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        #Movement flag
        self.movingRight = False
        self.movingLeft = False
        
    #Methods
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        #Update the ship's center value, not the rect
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.center += self.settings.shipSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.settings.shipSpeedFactor
        
        #Update the rect object from self.center
        self.rect.centerx = self.center
    def centerShip(self):
        self.center = self.screenRect.centerx