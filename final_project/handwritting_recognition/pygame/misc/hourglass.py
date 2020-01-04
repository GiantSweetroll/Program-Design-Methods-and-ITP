from pygame.rect import Rect

from final_project.handwritting_recognition import file_operation

class Hourglass():
    
    #Constructor
    def __init__(self):
        
        self.__index:int = 0
        self.__images:[] = file_operation.load_hourglass_images()
        
        #Create rect object (since all the images have same size, just use the first one to measure the width and height)
        self.__rect:Rect = Rect(0, 0, 
                                self.__images[0].get_rect().width, 
                                self.__images[0].get_rect().height)
    
    #Setters and Getters
    def get_rect(self):
        """Returns the rect object that will be used to place the hourglass images"""
        return self.__rect
    
    #Other Methods
    def next(self):
        """Increment the image index of the hourglass image by one"""
        if self.__index + 1 >= len(self.__images):
            self.__index = 0
        else:
            self.__index =+ 1
            
    def draw(self, screen):
        """Draw the hourglass to the screen"""
        screen.blit(self.__images[self.__index], self.__rect)