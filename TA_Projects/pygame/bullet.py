import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    #Constructor
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        #Create a bullet rect at (0,0) and then set correct position (ship's position)
        self.rect = pygame.Rect(0, 0, settings.bulletWidth, settings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = settings.bulletColor
        self.speedFactor = settings.bulletSpeedFactor
        
    
    #Methods
    def update(self):
        #Move the bullet up the screen
        self.y -= self.speedFactor
        #Update rect position
        self.rect.y = self.y
        
    def drawBullet(self):
        #Draw bullet to screen
        pygame.draw.rect(self.screen, self.color, self.rect)