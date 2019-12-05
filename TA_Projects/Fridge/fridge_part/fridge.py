from TA_Projects.Fridge.fridge_part.freezer import Freezer
from TA_Projects.Fridge.fridge_part.fridge_body import FridgeBody
class Fridge():
    
    #Fields
    freezer:Freezer
    body:FridgeBody
    
    #Constructor
    def __init__(self):
        self.freezer = Freezer()
        self.body = FridgeBody()