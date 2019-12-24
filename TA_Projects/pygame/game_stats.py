class GameStats():
    
    #Constructor
    def __init__(self, settings):
        self.settings = settings
        self.resetStats()
        #Start alien invasion in an inactive statew
        self.gameActive = False
        
        #High score should never be reset
        self.highScore = 0
    
    #Methods
    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit
        self.score = 0
        self.level = 1