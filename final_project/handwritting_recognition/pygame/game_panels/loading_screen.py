from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
from final_project.handwritting_recognition.pygame import globals
from final_project.handwritting_recognition.pygame.misc.hourglass import Hourglass
from final_project.handwritting_recognition import file_operation, constants,\
    methods
from final_project.handwritting_recognition.pygame.misc.console import Console
from random import random
from final_project.handwritting_recognition.neural_network import NeuralNetwork


class LoadingScreen(Panel):
    
    #Constructor
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        
        #Initialize components
        self.__loading_progress_label:Label = Label(globals.loading_progress)
        self.__hourglass:Hourglass = Hourglass()
        self.__ai:AI = None
        self.__ai_image = Console()
        self.__loading_finished:bool = None
        self.__loading_hint_label:Label = Label()
        self.__loading_hints:[str] = file_operation.load_loading_hints()
        self.__ai_guess_display:Console = Console(constants.path_img_ai_info_empty)
        self.__ai_guess_label:Label = Label()
        
        self.__thread_progress:Thread = None
        self.__thread_ai_iamge:Thread = None
        self.__thread_loading_hints:Thread = None
        self.__thread_nn:Thread = None
        
        #Component placements
        padding:int = 10
        screen_rect:Rect = self.get_screen().get_rect()
        #AI Image
        self.__ai_image.get_rect().centery = screen_rect.centery
        self.__ai_image.get_rect().right = screen_rect.centerx - padding
        #AI guess display
        self.__ai_guess_display.get_rect().left = screen_rect.centerx + padding
        self.__ai_guess_display.get_rect().centery = screen_rect.centery
        #AI guess label
        self.__ai_guess_label.get_rect().left = self.__ai_guess_display.get_rect().left
        self.__ai_guess_label.get_rect().top = self.__ai_guess_display.get_rect().centery
        #Loading hints
        self.__loading_hint_label.get_rect().centery = screen_rect.bottom - self.__loading_hint_label.get_rect().height
        #Loading progress label and hourglass
        self.__loading_progress_label.get_rect().top = screen_rect.top + 20
        self.__hourglass.get_rect().top =  self.__loading_progress_label.get_rect().top
        #Other component placements are configured dynamically
    
    #Methods for multi-threading
    def display_loading_hints(self):
        """Method to display the loading hints"""
        msg:str = random.choice(self.__loading_hints) if not self.__loading_finished else self.__loading_hint_label.get_text()
        
        self.__loading_hint_label.set_text(msg, True)
        self.__loading_hint_label.draw(self.get_screen())
    
    def display_loading_progress(self):
        """Method to display the loading progress messages and hourglass animation"""
        progress:str = globals.loading_progress
        if progress != self.__loading_progress_label.get_text():
            #Only update when needed
            self.__loading_progress_label.set_text(progress, True)
            
            #Update positions
            self.__loading_progress_label.get_rect().centerx = self.get_screen().get_rect().centerx - self.__hourglass.get_rect().width
            self.__hourglass.get_rect().left = self.__loading_progress_label.get_rect().right
        
        self.__hourglass.next()     #Update hourglass animation
        
        #Draw
        self.__loading_progress_label.draw(self.get_screen())
        self.__hourglass.draw(self.get_screen())
    
    def display_ai_and_guess(self):
        """Method to display the AI image and guess display screen"""
        
        #Set AI Image
        self.__ai_image.set_image(self.__ai.get_image_processing_path())
        
        #Pick guess by random
        guess:str = random.choice(constants.char_list) if not self.__loading_finished else ":)"
        self.__ai_guess_label.set_text(guess, True)
        
        #Display guess
        self.get_screen().blit(self.__ai_guess_display, self.__ai_guess_display.get_rect())
        self.__ai_guess_display.draw(self.get_screen())
        #Display AI Image
        self.__ai_image.draw(self.get_screen())
    
    def load_neural_network_and_predict(self) -> str:
        """Loads the neural network of the specified AI"""
        #Load neural network
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
        return prediction
        
    #Overridden Methods
    def check_events(self, event):
        super().check_events(event)
    
    def draw_components(self):
        super().draw_components()
        
        if globals.loading_active:
            if self.__loading_finished != True:
                #TO-DO
                pass
        