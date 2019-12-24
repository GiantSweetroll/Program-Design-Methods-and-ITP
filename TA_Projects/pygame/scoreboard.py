import pygame
from pygame.sprite import Group

from TA_Projects.pygame.ship import Ship


class Scoreboard():
    
    #Constructor
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        
        #Font setting for scoring information
        self.textColor = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Prepare the initial score image
        self.prepScore()
        self.prepHighScore()
        self.prepLevel()
        self.prepShips()
    
    #Methods
    def prepScore(self):
        roundedScore = round(self.stats.score, -1)
        scoreStr =  "{:,}".format(roundedScore)
        self.scoreImg = self.font.render(scoreStr, True, self.textColor, self.settings.backgroundColor)
        
        #Display the score at the top right of the screen
        self.scoreRect = self.scoreImg.get_rect()
        self.scoreRect.right = self.screenRect.right-20
        self.scoreRect.top = 20
    
    def prepHighScore(self):
        highScore = round(self.stats.highScore, -1)
        highScoreStr = "{:,}".format(highScore)
        self.highScoreImg = self.font.render(highScoreStr, True, self.textColor, self.settings.backgroundColor)
        
        #Center the high score
        self.highScoreRect = self.highScoreImg.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top
    
    def prepLevel(self):
        self.levelImg = self.font.render(str(self.stats.level), True, self.textColor, self.settings.backgroundColor)
        
        #Position the level below the score
        self.levelRect = self.levelImg.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom+10
    
    def prepShips(self):
        self.ships = Group()
        for shipNumber in range(self.stats.shipsLeft):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def showScore(self):
        self.screen.blit(self.scoreImg, self.scoreRect)
        self.screen.blit(self.highScoreImg, self.highScoreRect)
        self.screen.blit(self.levelImg, self.levelRect)
        self.ships.draw(self.screen)