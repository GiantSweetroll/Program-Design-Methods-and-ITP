class Settings():
    
    #Fields
    screen_width:int
    screen_height:int
    background_color:()
    pen_color:()
    pen_size:int
    eraser_size:int
    
    #Constructor
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 760
        self.background_color = (255, 255, 255)
        self.pen_color = (0, 0, 0)
        self.pen_size = 10