import pygame.font

class Button():
    
    #Constructor
    def __init__(self, screen, msg, width:int = 200, height:int = 50, button_color:() = (0, 255, 0), text_color:() = (255, 255, 255)):
        self.screen = screen
        self.screenRect = screen.get_rect()
        
        #Set the dimensions and properties of the button
        self.width, self.height = width, height
        self.__button_color = button_color
        self.__text_color = text_color
        self.__msg = msg
        self.__font = pygame.font.SysFont(None, 48)
        self.__text = msg
        
        #Build the button's rect object and center it
        self.__rect = pygame.Rect(0, 0, self.width, self.height)
        self.__rect.center = self.screenRect.center
        
        #The button message needs to be prepped only once
        self.prep_msg(msg)
    
    #Setters and Getters
    get_button_color = lambda self: self.__button_color
    get_text_color = lambda self: self.__text_color
    get_text = lambda self: self.__text
    get_font = lambda self: self.__font
    get_rect = lambda self: self.__rect
    get_msg_img = lambda self: self.__msgImg
    get_msg_img_rect = lambda self: self.__msgImgRect
    def set_button_color(self, color:()):
        """Set color of button"""
        self.__button_color = color
    def set_text_color(self, color:()):
        """Set color of text"""
        self.__text_color = color
    def set_text(self, msg):
        """Set the text message"""
        self.__msg = msg
    def set_font(self, font):
        self.__font = font
    def set_rect(self, rect):
        self.__rect = rect
    #Other Methods
    def prep_msg(self, msg):
        self.__msgImg = self.__font.render(msg, True, self.__text_color, self.__button_color)
        self.__msgImgRect = self.__msgImg.get_rect()
        self.__msgImgRect.center = self.__rect.center
    def draw_button(self):
        #Draw blank button and then draw message
        self.screen.fill(self.__button_color, self.__rect)
        self.screen.blit(self.__msgImg, self.__msgImgRect)