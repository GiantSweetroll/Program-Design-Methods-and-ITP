from TA_Projects.Fridge.item.item import Item
class Beverage(Item):
    
    #Fields
    ALCOHOL:str = "Alcohol"
    JUICE:str = "Juice"
    MILK:str = "Milk"
    COFFEE:str = "Coffee"
    TEA:str = "Tea"
    SYRUP:str = "Syrup"
    WATER:str = "Water"
    
    #Constructor
    def __init__(self, name:str, size:int, bevType:str, prefferedStorage = Item.STORE_COLD):
        super().__init__(name, size, prefferedStorage, "Beverage", bevType)
        self.__type = bevType