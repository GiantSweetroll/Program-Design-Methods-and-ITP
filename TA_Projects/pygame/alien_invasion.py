import pygame
from pygame.sprite import Group

from TA_Projects.pygame import game_functions as gf
from TA_Projects.pygame.button import Button
from TA_Projects.pygame.game_stats import GameStats
from TA_Projects.pygame.settings import Settings
from TA_Projects.pygame.ship import Ship
from TA_Projects.pygame.scoreboard import Scoreboard


def runGame():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    
    #Make the Play Button
    playButton = Button(settings, screen, "Play")
    
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(settings, screen) #Make ship
    bullets = Group()
    aliens = Group()
    
    #Create fleet of aliens
    gf.createFleet(settings, screen, ship, aliens)
    
    #Main game process
    while True:
        gf.checkEvents(settings, screen, stats, sb, playButton, ship, aliens, bullets)
        
        if stats.gameActive:
            ship.update()
            gf.updateBullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.updateAliens(settings, stats, screen, sb, ship, aliens, bullets)
        
        gf.updateScreen(settings, screen, stats, sb, aliens, ship, bullets, playButton)
        
runGame()