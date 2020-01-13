import random
from threading import Thread
import time

import pygame

from final_project.handwritting_recognition import file_operation, constants, \
    methods
from final_project.handwritting_recognition.neural_network import NeuralNetwork
from final_project.handwritting_recognition.pygame import globals
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
from final_project.handwritting_recognition.pygame.misc.hourglass import Hourglass
from final_project.handwritting_recognition.pygame.misc.image_panel import ImagePanel


class LoadingScreen(Panel):
    
    #Constructor
    def __init__(self, screen, settings):
        super().__init__(screen, settings, background_img_path="loading.png")
        
        #Initialize components
        self.__loading_progress_label:Label = Label(globals.loading_progress)
        self.__hourglass:Hourglass = Hourglass()
        self.__ai:AI = None
        self.__ai_image = ImagePanel()
        self.__loading_finished:bool = None
        self.__loading_hint_label:Label = Label(font_size=30)
        self.__loading_hints:[str] = file_operation.load_loading_hints()
        self.__ai_guess_display:ImagePanel = ImagePanel(constants.path_img_empty_screen)
        self.__ai_guess_label:Label = Label(font_size=500)
        
        self.__thread_progress:Thread = None
        self.__thread_ai_image:Thread = None
        self.__thread_loading_hints:Thread = None
        self.__thread_nn:Thread = None
        
        #Component placements
        self.__padding:int = 20
        screen_rect:Rect = self.get_screen().get_rect()
        #AI guess display
        self.__ai_guess_display.get_rect().left = screen_rect.centerx + self.__padding
        self.__ai_guess_display.get_rect().centery = screen_rect.centery
        #AI guess label
        self.__ai_guess_label.get_rect().centery = self.__ai_guess_display.get_rect().centery
        #Loading hints
        self.__loading_hint_label.get_rect().centery = screen_rect.bottom - self.__loading_hint_label.get_rect().height
        #Loading progress label and hourglass
        self.__loading_progress_label.get_rect().top = screen_rect.top + 20
        self.__hourglass.get_rect().top =  self.__loading_progress_label.get_rect().top
        #Other component placements are configured dynamically
    
    #Methods for multi-threading
    def display_loading_hints(self):
        """Method to display the loading hints"""
        msg:str = random.choice(self.__loading_hints)   #Pick a text by random
        self.__loading_hint_label.set_text(msg, True)
        self.__loading_hint_label.get_rect().centerx = self.get_screen().get_rect().centerx #Update label position
        time.sleep(5.0)
    
    def display_loading_progress(self):
        """Method to display the loading progress messages and hourglass animation"""
        progress:str = globals.loading_progress
        if progress != self.__loading_progress_label.get_text():    #Only update when needed
            self.__loading_progress_label.set_text(progress, True)
            
            #Update positions
            self.__loading_progress_label.get_rect().centerx = self.get_screen().get_rect().centerx - self.__hourglass.get_rect().width
            self.__hourglass.get_rect().left = self.__loading_progress_label.get_rect().right
            self.__hourglass.get_rect().centery = self.__loading_progress_label.get_rect().centery
        
        self.__hourglass.next()     #Update hourglass animation
        time.sleep(0.08)
    
    def display_guess(self):
        """Method to display AI's guess display screen"""
        #Pick guess by random
        guess:str = random.choice(constants.char_list) if not self.__loading_finished else ":)"
        self.__ai_guess_label.set_text(guess, True)
        self.__ai_guess_label.get_rect().centerx = self.__ai_guess_display.get_rect().centerx
        time.sleep(0.2)
    
    def load_neural_network_and_predict(self):
        """Loads the neural network of the specified AI"""
        #Load neural network
        self.__loading_finished = False
        methods.update_loading_progress("Loading neural network...")
        nn:NeuralNetwork = self.__ai.load_neural_network()
        
        #Load input
        methods.update_loading_progress("Loading input...")
        image = file_operation.load_image(constants.pygame_image_path + constants.pygame_test_image_name)
        methods.update_loading_progress("Formatting input...")
        image = methods.prepare_images_for_mlp_input([image])
        
        #Prediction
        methods.update_loading_progress("Making prediction...")
        prediction = nn.predict(image[0].reshape(1, constants.image_width, 
                                                constants.image_height, 
                                                constants.color_channels), False)
        
        methods.update_loading_progress("Prediction complete!")
        globals.prediction = prediction
        self.__loading_finished = True
        time.sleep(2.0)
        globals.panel_index += 1
        globals.show_results = True
    
    #Other Methods
    def __check_thread(self, thread:Thread, target):
        """DO NOT USE - DEPRECATED"""
        #This method should not be used, as it created infinite amounts of the same thread....
        if thread == None or not thread.is_alive():
            thread = Thread(target = target)   #Initialize the thread
            thread.start()  #Start the thread
    
    #Overridden Methods
    def check_events(self, event):
        super().check_events(event)
    
    def draw_components(self):
        super().draw_components()
        
        if globals.loading_active:
            #Check AI:
            if self.__ai == None:
                self.__ai = globals.active_ai
                self.__ai_image.set_image(self.__ai.get_image_processing_path())
                
                #Positioning ai image
                self.__ai_image.get_rect().centery = self.get_screen().get_rect().centery
                self.__ai_image.get_rect().right = self.get_screen().get_rect().centerx - self.__padding
            
            #Check Thread status
            if self.__thread_loading_hints == None or not self.__thread_loading_hints.is_alive():
                self.__thread_loading_hints = Thread(target=self.display_loading_hints)
                self.__thread_loading_hints.start()
            if self.__thread_ai_image == None or not self.__thread_ai_image.is_alive():
                self.__thread_ai_image = Thread(target=self.display_guess)
                self.__thread_ai_image.start()
            if self.__thread_progress == None or not self.__thread_progress.is_alive():
                self.__thread_progress = Thread(target=self.display_loading_progress)
                self.__thread_progress.start()
            #Check neural network thread
            if self.__thread_nn == None:
                self.__thread_nn = Thread(target=self.load_neural_network_and_predict)
                self.__thread_nn.start()
            
            #Draw components
            #Display loading hints
            self.__loading_hint_label.draw(self.get_screen())
            #Display loading progress and hourglass
            self.__loading_progress_label.draw(self.get_screen())
            self.__hourglass.draw(self.get_screen())
            #Display guess
            self.__ai_image.draw(self.get_screen())
            self.__ai_guess_display.draw(self.get_screen())
            self.__ai_guess_label.draw(self.get_screen())
            #Display AI Image
            self.__ai_image.draw(self.get_screen())

        pygame.display.flip()
    
    def reset_defaults(self):
        super().reset_defaults()
        self.__init__(self.get_screen(), self.get_settings())