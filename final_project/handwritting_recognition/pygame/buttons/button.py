import pygame
from pygame.surface import Surface

from final_project.handwritting_recognition.pygame.settings import Settings


class Button():
    
    #Constructor
    def __init__(self, 
                 screen, 
                 settings:Settings, 
                 msg, 
                 width:int = 200, 
                 height:int = 50,
                 font = None,
                 button_color:() = (23, 74, 211, 220), 
                 text_color:() = (255, 255, 255),
                 padding:int = 3):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        
        #Set the dimensions and properties of the button
        self._disabled_color:() = settings.button_color_disabled
        self._enabled_color:() = button_color
        self._width, self._height = width + padding*2, height + padding*2
        self.__button_color = button_color if button_color != None else (255, 255, 255, 0)
        self.__text_color = text_color
        self.__font = font if font != None else settings.button_text_font
        self.__text = msg
        txt_width, txt_height = self.__font.size(self.__text)
        self._width = txt_width + padding*2 if self._width < txt_width else self._width
        self._height = txt_height + padding*2 if self._height < txt_height else self._height
        self.__action_command:str = self.get_text() #used for button action identifiers, similar to Java's ActionCommand
        self.__enabled:bool = True
        
        
        self._prepare_button_and_text()
    
    #Setters and Getters
    get_width = lambda self: self._width
    get_height = lambda self: self._height
    get_button_color = lambda self: self.__button_color
    get_text_color = lambda self: self.__text_color
    get_text = lambda self: self.__text
    get_font = lambda self: self.__font
    get_rect = lambda self: self.__rect
    get_msg_img = lambda self: self.__msgImg
    get_msg_img_rect = lambda self: self.__msgImgRect
    get_action_command = lambda self: self.__action_command
    get_disabled_color = lambda self: self._disabled_color
    is_enabled = lambda self: self.__enabled
    def set_width(self, width:int):
        """Set width of the button, button is recreated after this method call"""
        self._width = width
        self._prepare_button_and_text()
        
    def set_height(self, height:int):
        """Set height of the button, button is recreated after this method call"""
        self._height = height
        self._prepare_button_and_text()
        
    def set_width_and_height(self, width:int, height:int):
        """Set the width and height of the button, button is recreated after this method call"""
        self._width = width
        self._height = height
        self._prepare_button_and_text()
        
    def set_button_color(self, color:()):
        """Set color of button"""
        self.__button_color = color
        self.prep_surface()
        
    def set_text_color(self, color:()):
        """Set color of text"""
        self.__text_color = color
        
    def set_text(self, msg):
        """Set the text message"""
        self.__text = msg
        self.prep_msg(msg)
        
    def set_font(self, font):
        """Set the font of the button text"""
        self.__font = font
        
    def set_rect(self, rect):
        """Set the rect of the button"""
        self.__rect = rect
        
    def set_action_command(self, string:str):
        """Sets the action command of the button"""
        self.__action_command = string
        
    def set_enabled(self, b:bool):
        """Enable or disable the button"""
        self.__enabled = b
        
        if (b): #enabled
            self.__button_color = self._enabled_color
        else:   #disabled
            self.__button_color = self.get_disabled_color()
        #recreate surface color and text
        self.prep_surface()
        self.prep_msg(self.get_text())
    
    #Other Methods
    def prep_msg(self, msg):
        self.__msgImg = self.__font.render(msg, True, self.__text_color, None)
        self.__msgImgRect = self.__msgImg.get_rect()
        self.__msgImgRect.center = self.__rect.center
        
    def draw(self):
        #Draw blank button and then draw message
#         self.screen.fill(self.__button_color, self.__rect)
        self.screen.blit(self.__surface, self.__rect)
        self.screen.blit(self.__msgImg, self.__msgImgRect)
        
    def _prepare_button_and_text(self):
        #Build the button's rect object and center it
        self.__rect = pygame.Rect(0, 0, self._width, self._height)
        self.__rect.center = self.screen_rect.center
        
        self.prep_surface()
        
        #The button message needs to be prepped only once
        self.prep_msg(self.get_text())
    
    def prep_surface(self):
        self.__surface = Surface(self.__rect.size, pygame.SRCALPHA)
        self.__surface.fill(self.__button_color)