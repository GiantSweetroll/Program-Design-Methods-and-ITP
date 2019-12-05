from TA_Projects.Fridge.container.container import Container
from TA_Projects.Fridge.fridge_part.fridge_part import FridgePart
from TA_Projects.Fridge.item.food import Food

class Freezer(FridgePart):
    
    #Fields
    iceCube:Container
    meat:Container
    shelf1:Container
    shelf2:Container
    
    #Constructor
    def __init__(self):
        super().__init__()
        self.iceCube = Container("Ice-Cube Container", 100, Food.ICE_CUBE)
        self.meat = Container("Frozen Meat Container", 100, Food.MEAT)
        self.shelf1 = Container("Upper Shelf", 30)
        self.shelf2 = Container("Lower Shelf", 30)
        
        self.addContainer(self.iceCube)
        self.addContainer(self.meat)
        self.addContainer(self.shelf1)
        self.addContainer(self.shelf2)
        