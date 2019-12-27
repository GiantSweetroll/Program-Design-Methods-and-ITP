import sys

import pygame
from pygame.rect import Rect

from final_project.handwritting_recognition import constants, methods,\
    file_operation
from final_project.handwritting_recognition.neural_network import NeuralNetwork
from final_project.handwritting_recognition.pygame import globals
from final_project.handwritting_recognition.pygame.settings import Settings


def check_events(neural_network, screen, settings, exit_button, guess_button, clear_button):
    """Method to check any keyboard or mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  #Stops game
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       #1 = Left click
                globals.mouse_left_pressed = True
                mouse_pos = get_mouse_position()
                check_clear_button(clear_button, mouse_pos)
                check_guess_button(neural_network, screen, settings, exit_button, guess_button, clear_button, mouse_pos)
                check_exit_button(exit_button, mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:       #1 = Left click
                globals.mouse_left_pressed = False

def update_screen(screen, settings, buttons_to_draw:[], guess_button_pressed:bool = False):
    """Method to update the game\'s screen"""
    screen.fill(settings.background_color)
    
    #Color pixel
    if globals.mouse_left_pressed:
        x, y = get_mouse_position()
        collide_with_button = False
        for button in buttons_to_draw:
            collide_with_button = button.get_rect().collidepoint(x, y)
            if collide_with_button:
                break
        if not collide_with_button and not guess_button_pressed:
            globals.colored_pixels.add((x, y))
    for pixel in globals.colored_pixels:
        pygame.draw.rect(screen, settings.pen_color, Rect(pixel[0], pixel[1], settings.pen_size, settings.pen_size))
    
    #Draw buttons
    for button in buttons_to_draw:
        button.draw_button()
    
    if not guess_button_pressed:
        pygame.display.flip()

def get_mouse_position() -> ():
    """Method to get the current coordinates of the mouse"""
    x, y = pygame.mouse.get_pos()
    return x, y

#Button presses
def check_clear_button(clear_button, mouse_pos:()):
    """Clear image when the clear button is clicked"""
    button_clicked = clear_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])
    if button_clicked:
        globals.colored_pixels.clear()
def check_exit_button(exit_button, mouse_pos:()):
    """Exit game when exit button is clicked"""
    button_clicked = exit_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])
    if button_clicked:
        sys.exit()  #Stops game
def check_guess_button(neural_network:NeuralNetwork, screen, settings:Settings, exit_button, guess_button, clear_button, mouse_pos:()):
    """Make prediction of drawn image when guess button is clicked"""
    button_clicked = guess_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])
    if button_clicked:
        #Remove the exit, guess, and clear buttons to capture only the drawn image
        globals.buttons_to_draw.clear()
        update_screen(screen, settings, globals.buttons_to_draw, guess_button_pressed=True)
        pygame.image.save(screen, constants.pygame_image_path + constants.pygame_test_image_name)     #Take a screenshot of the game screen window and save it to disk
        globals.buttons_to_draw = [exit_button, guess_button, clear_button] #Add the buttons back
        #Link to neural network prediction
        image = file_operation.load_image(constants.pygame_image_path + constants.pygame_test_image_name)
        image = methods.prepare_images_for_mlp_input([image])
        prediction = neural_network.predict(image[0].reshape(1, constants.image_width, 
                                                constants.image_height, 
                                                constants.color_channels), False)
        print(prediction)
        