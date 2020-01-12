import sys

import pygame
from pygame.rect import Rect

from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.settings import Settings


def create_screen(settings:Settings):
    """Create the pygame screen"""
    return pygame.display.set_mode((settings.screen_width, settings.screen_height))

def check_events(panel:Panel):
    """Method to check any keyboard or mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  #Stops game
        panel.check_events(event)   #Check for events in the current panel

def update_screen(screen, settings:Settings, panel:Panel):
    """Method to update the game\'s screen"""
    screen.fill(settings.background_color)
    panel.draw_components()

def get_mouse_position() -> ():
    """Method to get the current coordinates of the mouse"""
    x, y = pygame.mouse.get_pos()
    return x, y

def mouse_in_area(rect:Rect, mouse_pos:()):
    """Returns True if the rect collides with the mouse pointer location (if coordinates are the same)"""
    return rect.collidepoint(mouse_pos[0], mouse_pos[1])

def mouse_on_button(button:Button, mouse_pos:()):
    """Check if the mouse pointer is on a button"""
    return mouse_in_area(button.get_rect(), mouse_pos)
        