from TA_Projects.Fridge.item.item import Item
class NonEdible(Item):
    
    #Fields
    POWER_GLUE:str = "Power Glue"
    TABLE:str = "Table"
    CHAIR:str = "Chair"
    TV:str = "TV"
    RADIO:str = "Radio"
    TOY:str = "Toy"
    LAPTOP:str = "Laptop"
    WET_TISSUES:str = "Wet Tissues"

    #Constructor
    def __init__(self, name:str, size:int, bevType:str, prefferedStorage = Item.STORE_COLD):
        super().__init__(name, size, prefferedStorage, "Non-Edible")
        self.__type = bevType