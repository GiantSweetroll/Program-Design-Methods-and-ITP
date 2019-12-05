class Item():
    
    #Fields
    STORE_FROZEN = "frozen" #Freezer
    STORE_COLD = "cold"     #Normal fridge space
    STORE_NORMAL = "normal" #Without cooling
    TYPE_DEFAULT = "Other"
    
    __name:str
    __size:int
    __prefferedStorage:str
    __itemClass:str
    __type:str
    
    #Constructor
    def __init__(self, name:str, size:int, prefferedStorage: str = Item.STORE_COLD, itemClass:str = Item.TYPE_DEFAULT, itemType:str = Item.TYPE_DEFAULT):
        self.__name = name
        self.__size = size
        self.__prefferedStorage = prefferedStorage
        self.__itemClass = itemClass
        self.__type = itemType
        
    #Setter and Getters
    def getName(self) -> str:
        return self.__name
    def setName(self, name:str):
        self.__name = name
    def getSize(self) -> int:
        return self.__size
    def setSize(self, size:int):
        self.__size = size
    def setPrefferedStorage(self, prefferedStorage:str):
        self.__prefferedStorage = prefferedStorage
    def getPrefferedStorage(self) -> str:
        return self.__prefferedStorage
    def getItemClass(self) -> str:
        return self.__itemClass
    def getItemType(self) -> str:
        return self.__type