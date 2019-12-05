class Person():
    
    #Fields
    __name:str
    __address:str
    
    #Constructor
    def __init__(self, name:str, address:str):
        self.__name = name
        self.__address = address
    
    #Methods
    def getName(self) -> str:
        return self.__name
    def getAddress(self) -> str:
        return self.__address
    def setAddress(self, address:str):
        self.__address = address
    def __str__(self) -> str:
        return self.getName() + "(" 