import pygame
from pygame.rect import Rect


class Label():
    """A text rect image, similar to Java JLabel"""
    
    #Constructor
    def __init__(self, 
                 text:str = "", 
                 font = None, 
                 font_type = None, 
                 font_size:int = 48, 
                 bold:bool = False, 
                 italic:bool = False, 
                 underline:bool = False, 
                 foreground_color:() = (0, 0, 0), 
                 background_color:() = None,
                 width:int = 200,
                 height:int = 50):
        """
        text: the text to be displayed in the label
        font: the font object (if this is specified, the font_type, font_size, bold, and italic params are ignored)
        font_type: the font family
        font_size = the size of the font
        bold: whether the text will be bolded
        italic: whether the text will be rendered with fake-italic
        underline: whether the text will be underlined
        foreground: the foreground color of the tet
        background_color: the background color of the label
        width: width of the label rect
        height: height of the label rect
        """
        
        #Initialize fields
        self.__font = pygame.font.SysFont(font_type, font_size, bold, italic) if font == None else font
        if underline:
            self.get_font().set_underline(True)
        self.__text:str = text
        self.__text_image = self.get_font().render(self.get_text(), True, foreground_color, background_color)
        self.__bgcolor:() = background_color if background_color != None else (255, 255, 255)
        self.__fgcolor:() = foreground_color if foreground_color != None else (0, 0, 0)
        
        txt_width, txt_height = self.__font.size(self.__text)
        self.__rect = Rect(0, 0, txt_width, txt_height)
        
        self.prep_text()
        
    #Setters and Getters
    def get_font(self):
        return self.__font
    
    def get_text(self):
        return self.__text
    
    def get_text_image(self):
        return self.__text_image
    
    def get_background_color(self) -> ():
        return self.__bgcolor
    
    def get_rect(self):
        return self.__rect
    
    def get_foreground_color(self) -> ():
        return self.__fgcolor
    
    def set_font(self, font):
        self.__font = font
        
    def set_text(self, text:str, render_text:bool = False):
        """
        text: the text
        render_text: whether to render the text image immediately (bool)
        """
        self.__text = text
        if render_text:
            self.prep_text()
    def set_text_image(self, text_image):
        self.__text_image = text_image
    def set_background_color(self, bgcolor:(), render_text:bool = False):
        """
        bgcolor: the background color in a set of RGB or RGBA tuples
        render_text: whether to render the text image immediately (bool)
        """
        self.__bgcolor = bgcolor
        if render_text:
            self.prep_text()   
    def set_foreground_color(self, fgcolor:(), render_text:bool = False):
        """
        fgcolor: the foreground color in a set of RGB or RGBA tuple
        render_text: whether to render the text image immediately (bool)
         """
        self.__fgcolor = fgcolor
        if render_text:
            self.prep_text()
    #Other Methods
    def draw(self, screen):
#         screen.fill(self.get_background_color(), self.get_rect())
        screen.blit(self.get_text_image(), self.get_rect(), special_flags=pygame.BLEND_RGBA_MULT)
        
    def prep_text(self):
        try:
            self.set_text_image(self.get_font().render(self.get_text(), True, self.get_foreground_color(), self.get_background_color()))
        except:
            pass
        txt_width, txt_height = self.__font.size(self.__text)
        self.__rect = Rect(self.__rect.left, self.__rect.top, txt_width, txt_height)
        self.get_text_image().get_rect().center = self.get_rect().center
        