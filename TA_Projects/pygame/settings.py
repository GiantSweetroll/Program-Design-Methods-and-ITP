class Settings():
    
    #Fields
    screenWidth:int
    screenHeight:int
    backgroundColor:()
    shipSpeedFactor:float
    
    #Constructor
    def __init__(self):
        #Screen settings
        self.screenWidth = 1366
        self.screenHeight = 768
        self.backgroundColor = (230, 230, 230)
        
        #Ship settings
        self.shipLimit = 3
        
        #Bullet settings
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = 60, 60, 60
        self.bulletsAllowed = 3
        
        #Alien settings
        self.fleetDropSpeed = 10
        
        #How quickly the game speeds up
        self.speedupScale = 1.1
        self.scoreScale = 1.5
        
        self.initDynamicSettings()
        
        #Scoring
        self.alienPoints = 50
    
    #Methods
    def initDynamicSettings(self):
        self.shipSpeedFactor = 1.5
        self.bulletSpeedFactor = 3
        self.alienSpeedFactor = 1
        self.fleetDirection = 1 #1 represents right, -1 represents left
    def increaseSpeed(self):
        self.shipSpeedFactor *= self.speedupScale
        self.bulletSpeedFactor *= self.speedupScale
        self.alienSpeedFactor *= self.speedupScale
        
        self.alienPoints = int(self.alienPoints * self.scoreScale)
        