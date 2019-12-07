from TA_Projects.Fridge.item.item import Item

class Container():
    
    #Fields
    ANY:str = "any10384"
    
    __space:int
    __prefItem:str
    __items:{}
    __name:str
    
    #Constructor
    def __init__(self, name:str, space:int, prefferedItem:str = ANY):
        self.__space = space
        self.__prefItem = prefferedItem
        self.__items = {}
        self.__name = name
    
    #Methods
    def getName(self) -> str:
        return self.__name
    def getMaxSpace(self) -> int:
        return self.__space
    def getSpaceLeft(self):
        total = 0
        for itemType in self.__items:
            for xType in self.__items[itemType]:
                for itemName in self.__items[itemType][xType]:
                    total += self.__items[itemType][xType][itemName]
        return self.__space - total
    def getPrefferedItem(self) -> str:
        return self.__prefItem
    
    def store(self, item:Item, amount:int = 1):
        itemClass:str = item.getItemClass()
        itemType:str = item.getItemType()
        if itemClass in self.__items:
            if itemType in self.__items[itemClass]:
                if item.getName() in self.__items[itemClass][itemType]:
                    self.__items[itemClass][itemType][item.getName()] += amount
                else:
                    self.__items[itemClass][itemType][item.getName()] = amount
            else:
                self.__items[itemClass][itemType] = {item.getName(): amount}
        else:
            self.__items[itemClass] = {itemType: {item.getName(): amount}}
            
    def removeAllItem(self, item:Item) -> bool:
        itemClass:str = item.getItemClass()
        if itemClass in self.__items:
            itemType:str = item.getItemType()
            if itemType in self.__items[itemClass]:
                if item.getName() in self.__items[itemClass][itemType]:
                    del(self.__items[itemClass][itemType][item.getName()])
                    return True
        return False
    def clear(self):
        self.__items = {}
    def removeItem(self, item:Item, amount:int) -> bool:
        itemClass:str = item.getItemClass()
        if itemClass in self.__items:
            itemType:str = item.getItemType()
            if itemType in self.__items[itemClass]:
                if item.getName() in self.__items[itemClass][itemType]:
                    self.__items[itemClass][itemType][item.getName()] -= amount
                    if self.__items[itemClass][itemType][item.getName()] <= 0:
                        del(self.__items[itemClass][itemType][item.getName()])
                    return True
        return False
    def getItemRemaining(self, item:Item) -> int:
        try:
            return self.__items[item.getItemClass()][item.getItemType()][item.getName()]
        except:
            return 0
    def getItemsList(self) -> {}:
        return self.__items