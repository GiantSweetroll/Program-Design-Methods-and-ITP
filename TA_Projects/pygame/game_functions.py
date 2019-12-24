import sys

import pygame

from TA_Projects.pygame.alien import Alien
from TA_Projects.pygame.bullet import Bullet
from TA_Projects.pygame import alien
from time import sleep


def checkEvents(settings, screen, stats, sb, playButton, ship, aliens, bullets):
    #Keyboard and mouse press
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  #Stops game
            elif event.type == pygame.KEYDOWN:
                checkKeyDownEvents(event, settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                checkKeyUpEvents(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                checkPlayButton(settings, screen, stats, sb, playButton, ship, aliens, bullets, mouseX, mouseY)

def checkKeyDownEvents(event, settings, screen, ship, bullets):
    #Respond to key presses
    if event.key == pygame.K_RIGHT:
        #Move the ship to the right
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(settings, screen, ship, bullets)

def checkKeyUpEvents(event, ship):
    if event.key == pygame.K_RIGHT:
        #Stop ship moving right
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
        
def shipHit(settings, stats, screen, sb, ship, aliens, bullets):    
    if stats.shipsLeft > 0:
        stats.shipsLeft -= 1    #Decrement shipsLeft
        
        #Update scoreboard
        sb.prepShips()
        
        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        
        #Create a new fleet and center the ship.
        createFleet(settings, screen, ship, aliens)
        ship.centerShip()
        
        #pause
        sleep(0.5)
    else:
        stats.gameActive = False
        pygame.mouse.set_visible(True)
        
def updateBullets(settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions.
    bullets.update()
    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    checkBulletAlienCollisions(settings, screen, stats, sb, ship, aliens, bullets)

def checkBulletAlienCollisions(settings, screen, stats, sb, ship, aliens, bullets):
    #Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alienPoints * len(aliens)
            sb.prepScore()
        checkHighScore(stats, sb)
    
    if len(aliens) == 0:
        #If the entire fleet is destroyed, start a new level
        bullets.empty()
        settings.increaseSpeed()
        createFleet(settings, screen, ship, aliens)
        
        #increase level
        stats.level += 1
        sb.prepLevel()

def fireBullet(settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    #Create new bullet
    if len(bullets) < settings.bulletsAllowed:
        newBullet = Bullet(settings, screen, ship)
        bullets.add(newBullet)

def createAlien(settings, screen, aliens, alienNumber, rowNumber):
    alien = Alien(settings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2* alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*rowNumber
    aliens.add(alien)

def createFleet(settings, screen, ship, aliens):
    #Create an alien and find the number of aliens in a row
    #Spacing between each alien is equal to one alien width
    alien = Alien(settings, screen)
    alienWidth = alien.rect.width
    numberAliensX = getNumberAliensX(settings, alienWidth)
    numberRows = getNumberRows(settings, ship.rect.height, alien.rect.height)
    
    #Create alien fleet
    for rowNumber in range(numberRows):
        #Create the first row of aliens
        for alienNumber in range(numberAliensX):
            #Create an alien and place it in the row
            createAlien(settings, screen, aliens, alienNumber, rowNumber)

def getNumberAliensX(settings, alienWidth):
    availableSpaceX = settings.screenWidth - 2*alienWidth
    numberAliensX = int(availableSpaceX/(2*alienWidth))
    return numberAliensX

def getNumberRows(settings, shipHeight, alienHeight):
    availableSpaceY = (settings.screenHeight - (3*alienHeight) - shipHeight)
    numberRows = int(availableSpaceY/(2*alienHeight))
    return numberRows

def updateAliens(settings, stats, screen, sb, ship, aliens, bullets):
    checkFleetEdges(settings, aliens)
    aliens.update()
    
    #Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(settings, stats, screen, sb, ship, aliens, bullets)
    
    #Look for alien hitting the bottom of the screen
    checkAliensBottom(settings, stats, screen, sb, ship, aliens, bullets)

def checkFleetEdges(settings, aliens):
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(settings, aliens)
            break

def changeFleetDirection(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleetDropSpeed
    settings.fleetDirection *= -1

def checkAliensBottom(settings, stats, screen, sb, ship, aliens, bullets):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            #Treat this the same as if the ship got hit
            shipHit(settings, stats, screen, sb, ship, aliens, bullets)
            break

def updateScreen(settings, screen, stats, sb, aliens, ship, bullets, playButton):
    screen.fill(settings.backgroundColor)
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
    
    #Draw score information
    sb.showScore()
    
    #Draw the play button if the game is inactive
    if not stats.gameActive:
        playButton.drawButton()    
    
    pygame.display.flip()   #Make the most recently drawn screen visible.

def checkPlayButton(settings, screen, stats, sb, playButton, ship, aliens, bullets, mouseX, mouseY):
    buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonClicked and not stats.gameActive:
        #Reset the game settings
        settings.initDynamicSettings()
        
        #Hide the mouse cursor
        pygame.mouse.set_visible(False)
        
        #Reset the game statistics
        stats.resetStats()
        stats.gameActive = True
        
        #Reset the scoreboard images
        sb.prepScore()
        sb.prepHighScore()
        sb.prepLevel()
        sb.prepShips()
        
        #Empty the list of aliens and bulelts
        aliens.empty()
        bullets.empty()
        
        #Create a new fleet and center the sheep
        createFleet(settings, screen, ship, aliens)
        ship.centerShip()
        
def checkHighScore(stats, sb):
    if stats.score > stats.highScore:
        stats.highScore = stats.score
        sb.prepHighScore()