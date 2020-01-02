import sys

import pygame
from pygame.rect import Rect

from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.settings import Settings


def create_screen(settings:Settings):
    return pygame.display.set_mode((settings.screen_width, settings.screen_height))

def check_events(panel:Panel):
    """Method to check any keyboard or mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  #Stops game
        panel.check_events(event)

def update_screen(screen, settings:Settings, panel:Panel):
    """Method to update the game\'s screen"""
    screen.fill(settings.background_color)
    panel.draw_components()

def get_mouse_position() -> ():
    """Method to get the current coordinates of the mouse"""
    x, y = pygame.mouse.get_pos()
    return x, y

def mouse_on_button(button:Button, mouse_pos:()):
    return mouse_in_area(button.get_rect(), mouse_pos)

def mouse_in_area(rect:Rect, mouse_pos:()):
    return rect.collidepoint(mouse_pos[0], mouse_pos[1])
        