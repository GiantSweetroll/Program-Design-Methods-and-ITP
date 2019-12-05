from TA_Projects.Fridge.item.item import Item
class Food(Item):
    
    #Fields
    VEGETABLE:str = "Vegetable"
    FRUIT:str = "Fruit"
    MEAT:str = "Meat"
    GRAIN:str = "Grain"
    DAIRY:str = "Dairy"
    EGG:str = "Egg"
    SOUP:str = "Soup"
    PUDDING:str = "Pudding"
    JELLY:str = "Jelly"
    ICE_CUBE:str = "Ice Cube"
    ICE_CREAM:str = "Ice-Cream"
    
    #Constructor
    def __init__(self, name:str, size:int, foodType:str, prefferedStorage = Item.STORE_COLD):
        super().__init__(name, size, prefferedStorage, "Food", foodType)