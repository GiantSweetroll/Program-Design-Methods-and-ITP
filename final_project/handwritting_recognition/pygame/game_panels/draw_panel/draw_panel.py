from abc import abstractclassmethod
import sys

import pygame
from pygame.event import Event
from pygame.rect import Rect

from final_project.handwritting_recognition.pygame import game_functions as gf
from final_project.handwritting_recognition.pygame import globals
from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
from final_project.handwritting_recognition.pygame.settings import Settings

class DrawPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings, sub_title_text:str = ""):
        super().__init__(screen, settings)
        
        #Fields initialization
        self._exit_button:Button = Button(self.get_screen(), self.get_settings(), "Exit", button_color = settings.button_color_red)
        self._guess_button:Button = Button(self.get_screen(), self.get_settings(), "Guess")
        self._clear_button:Button = Button(self.get_screen(), self.get_settings(), "Clear")
        self._buttons_to_draw:[Button] =   [self._exit_button, self._guess_button, self._clear_button]
        self._guess_button_pressed:boolean = False
        self.__colored_pixels = set(())
        self._sub_title_label:Label = Label(sub_title_text)
        self._draw_sub_title_label:bool = False
        
        #Configure button placements
        screen_rect = self.get_screen().get_rect()
        #Sub title
        self._sub_title_label.get_rect().top = screen_rect.top + 20
        self._sub_title_label.get_rect().centerx = screen_rect.centerx
        #Exit button
        self.get_exit_button().get_rect().left = screen_rect.left + 20
        self.get_exit_button().get_rect().centery = screen_rect.bottom - self.get_exit_button().get_height()
        self.get_exit_button().prep_msg(self.get_exit_button().get_text())
        #Guess button
        self.get_guess_button().get_rect().centery = screen_rect.bottom - self.get_guess_button().get_height()
        self.get_guess_button().prep_msg(self.get_guess_button().get_text())
        #Clear button
        self.get_clear_button().get_rect().right =screen_rect.right - 20
        self.get_clear_button().get_rect().centery = screen_rect.bottom - self.get_clear_button().get_height()
        self.get_clear_button().prep_msg(self.get_clear_button().get_text())
    
    #Setters and Getters
    def set_draw_sub_title_label(self, b:bool):
        """Method whether to draw the sub title label or not"""
        self._draw_sub_title_label = b
    
    def set_guess_button_pressed(self, b:bool):
        """Method to identify whether the guess button was pressed"""
        self._guess_button_pressed = b
    
    def get_exit_button(self):
        """Returns the exit button object"""
        return self._exit_button
    
    def get_guess_button(self):
        """Returns the guess button object"""
        return self._guess_button
    
    def get_clear_button(self):
        """Returns the clear button object"""
        return self._clear_button
    
    def get_buttons_to_draw(self):
        """Returns the list of buttons that should be drawn on the screen"""
        return self._buttons_to_draw
    
    #Other Methods
    def check_clear_button(self, mouse_pos:()):
        """Clear image when the clear button is clicked"""
        if gf.mouse_on_button(self._clear_button, mouse_pos):
            self.__colored_pixels.clear()
            self.set_screen(gf.create_screen(self.get_settings()))
            
    def check_exit_button(self, mouse_pos:()):
        """Exit game when exit button is clicked"""
        if gf.mouse_on_button(self._exit_button, mouse_pos):
            sys.exit()  #Stops game
    
    def draw_art(self):
        """Method to draw the mouse click art"""
        if globals.mouse_left_pressed:
            x, y = gf.get_mouse_position()
            collide_with_button = False
            for button in self._buttons_to_draw:
                collide_with_button = button.get_rect().collidepoint(x, y)  #Check if the drawing will collide with the buttons
                if collide_with_button:
                    break
            if not collide_with_button and not self._guess_button_pressed:
                self.__colored_pixels.add((x, y))
        for pixel in self.__colored_pixels:
            pygame.draw.rect(self.get_screen(), 
                             self.get_settings().pen_color, 
                             Rect(pixel[0], 
                                  pixel[1], 
                                  self.get_settings().pen_size, 
                                  self.get_settings().pen_size))
    
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
        #Draw sub title
        if self._draw_sub_title_label:
            self._sub_title_label.draw(self.get_screen())
        
        #Color pixel
        if not self._guess_button_pressed:
            self.draw_art()
        
        #Draw buttons
        for button in self._buttons_to_draw:
            button.draw()
        
        if not self._guess_button_pressed:
            pygame.display.flip()
        else:
            self.get_screen().fill(self.get_settings().background_color)
            self.draw_art()
            self._guess_button_pressed = False
    
    def reset_defaults(self):
        super().reset_defaults()
        self.__colored_pixels.clear()
    
    #Abstract Methods
    @abstractclassmethod
    def check_guess_button(self, mouse_pos:()):
        pass
    