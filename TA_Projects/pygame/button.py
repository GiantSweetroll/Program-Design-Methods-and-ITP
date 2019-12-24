import pygame.font

class Button():
    
    #Constructor
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screenRect = screen.get_rect()
        
        #Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.buttonColor = (0, 255, 0)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center
        
        #The button message needs to be prepped only once
        self.prepMsg(msg)
        
    
    #Methods
    def prepMsg(self, msg):
        self.msgImg = self.font.render(msg, True, self.textColor, self.buttonColor)
        self.msgImgRect = self.msgImg.get_rect()
        self.msgImgRect.center = self.rect.center
    def drawButton(self):
        #Draw blank button and then draw message
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImg, self.msgImgRect)