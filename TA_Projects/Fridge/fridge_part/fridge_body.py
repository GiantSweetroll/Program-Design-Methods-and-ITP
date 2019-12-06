from TA_Projects.Fridge.container.container import Container
from TA_Projects.Fridge.fridge_part.fridge_part import FridgePart
from TA_Projects.Fridge.item.food import Food
from TA_Projects.Fridge.item.beverage import Beverage

class FridgeBody(FridgePart):
    
    #Fields
    general:Container
    fruits:Container
    vegetables:Container
    eggs:Container
    shelfTop:Container
    shelfDrink1:Container
    shelfDrink2:Container
    shelfSmall:Container
    
    #Constructor
    def __init__(self):
        super().__init__("Main Fridge")
        self.general = Container("General Shelf", 200)
        self.fruits = Container("Fruits Basket", 100, Food.FRUIT)
        self.vegetables = Container("Vegetables Container", 200, Food.VEGETABLE)
        self.eggs = Container("Eggs Rack", 20, Food.EGG)
        self.shelfTop = Container("Top Shelf", 50)
        self.shelfDrink1 = Container("Upper Drinks Shelf", 30, Beverage.SYRUP)
        self.shelfDrink2 = Container("Lower Drinks Shelf", 30, Beverage.MILK)
        self.shelfSmall = Container("Small Shelf", 10)
        
        self.addContainer(self.general)
        self.addContainer(self.fruits)
        self.addContainer(self.vegetables)
        self.addContainer(self.eggs)
        self.addContainer(self.shelfTop)
        self.addContainer(self.shelfSmall)
        self.addContainer(self.shelfDrink1)
        self.addContainer(self.shelfDrink2)
