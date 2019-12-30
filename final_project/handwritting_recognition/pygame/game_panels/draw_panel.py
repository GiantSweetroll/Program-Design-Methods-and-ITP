import sys

import pygame
from pygame.event import Event
from pygame.rect import Rect

import final_project.handwritting_recognition.pygame.globals as globals
from final_project.handwritting_recognition import constants, file_operation, \
    methods
from final_project.handwritting_recognition.neural_network import NeuralNetwork
from final_project.handwritting_recognition.pygame import game_functions as gf
from final_project.handwritting_recognition.pygame.buttons.clear_button import ClearButton
from final_project.handwritting_recognition.pygame.buttons.exit_button import ExitButton
from final_project.handwritting_recognition.pygame.buttons.guess_button import GuessButton
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.settings import Settings


class DrawPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings, neural_network:NeuralNetwork = None):
        super().__init__(screen, settings)
        
        #Fields initialization
        self.__exit_button:Button = ExitButton(self.get_screen(), self.get_settings())
        self.__guess_button:Button = GuessButton(self.get_screen(), self.get_settings())
        self.__clear_button:Button = ClearButton(self.get_screen(), self.get_settings())
        self.__buttons_to_draw:[Button] =   [self.__exit_button, self.__guess_button, self.__clear_button]
        self.__guess_button_pressed:boolean = False
        self.__colored_pixels = set(())
        self.__neural_network = neural_network
        
        #Configure button placements
        #Exit button
        self.get_exit_button().get_rect().left = self.get_screen().get_rect().left + 20
        self.get_exit_button().get_rect().centery = self.get_screen().get_rect().bottom - self.get_exit_button().height
        self.get_exit_button().prep_msg(self.get_exit_button().get_text())
        #Guess button
        self.get_guess_button().get_rect().centery = self.get_screen().get_rect().bottom - self.get_guess_button().height
        self.get_guess_button().prep_msg(self.get_guess_button().get_text())
        #Clear button
        self.get_clear_button().get_rect().right = self.get_screen().get_rect().right - 20
        self.get_clear_button().get_rect().centery = self.get_screen().get_rect().bottom - self.get_clear_button().height
        self.get_clear_button().prep_msg(self.get_clear_button().get_text())
    
    #Setters and Getters
    def get_exit_button(self):
        """Returns the exit button object"""
        return self.__exit_button
    def get_guess_button(self):
        """Returns the guess button object"""
        return self.__guess_button
    def get_clear_button(self):
        """Returns the clear button object"""
        return self.__clear_button
    def get_neural_network(self):
        """Returns the selected neural network"""
        return self.__neural_network
    def set_neural_network(self, neural_network:NeuralNetwork):
        self.__neural_network = neural_network
    
    #Other Methods
    def check_clear_button(self, mouse_pos:()):
        """Clear image when the clear button is clicked"""
        button_clicked = self.__clear_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])
        if button_clicked:
            self.__colored_pixels.clear()
            self.set_screen(gf.create_screen(self.get_settings()))
    def check_exit_button(self, mouse_pos:()):
        """Exit game when exit button is clicked"""
        button_clicked = self.__exit_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])
        if button_clicked:
            sys.exit()  #Stops game
    def check_guess_button(self, mouse_pos:()):
        """Make prediction of drawn image when guess button is clicked"""
        if self.__neural_network != None:   #Check if the neural network has been specified
            button_clicked = self.__guess_button.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])
            if button_clicked:
                self.__guess_button_pressed = True
                #Remove the exit, guess, and clear buttons to capture only the drawn image
                self.__buttons_to_draw.clear()
                self.draw_components()
                pygame.image.save(self.get_screen(), constants.pygame_image_path + constants.pygame_test_image_name)     #Take a screenshot of the game screen window and save it to disk
                self.__buttons_to_draw = [self.__exit_button, self.__guess_button, self.__clear_button] #Add the buttons back
                #Link to neural network prediction
                image = file_operation.load_image(constants.pygame_image_path + constants.pygame_test_image_name)
                image = methods.prepare_images_for_mlp_input([image])
                prediction = self.__neural_network.predict(image[0].reshape(1, constants.image_width, 
                                                        constants.image_height, 
                                                        constants.color_channels), False)
                print(prediction)
        else:
            print("Neural Network not yet specified")
    
    #Overridden Methods
    def check_events(self, event:Event):
        super().check_events(event)
        
        #Check mouse button press
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       #1 = Left click
                globals.mouse_left_pressed = True
                mouse_pos = gf.get_mouse_position()
                self.check_clear_button(mouse_pos)
                self.check_guess_button(mouse_pos)
                self.check_exit_button(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:       #1 = Left click
                globals.mouse_left_pressed = False
    def draw_components(self):
        super().draw_components()
        
        #Color pixel
        if globals.mouse_left_pressed:
            x, y = gf.get_mouse_position()
            collide_with_button = False
            for button in self.__buttons_to_draw:
                collide_with_button = button.get_rect().collidepoint(x, y)  #Check if the drawing will collide with the buttons
                if collide_with_button:
                    break
            if not collide_with_button and not self.__guess_button_pressed:
                self.__colored_pixels.add((x, y))
        for pixel in self.__colored_pixels:
            pygame.draw.rect(self.get_screen(), 
                             self.get_settings().pen_color, 
                             Rect(pixel[0], 
                                  pixel[1], 
                                  self.get_settings().pen_size, 
                                  self.get_settings().pen_size))
        
        #Draw buttons
        for button in self.__buttons_to_draw:
            button.draw_button()
        
        if not self.__guess_button_pressed:
            pygame.display.flip()
        else:
            self.__guess_button_pressed = False