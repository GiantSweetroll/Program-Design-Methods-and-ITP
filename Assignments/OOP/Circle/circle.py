import math

class Circle():
    
    #Fields
    __radius:float
    __color:str
    
    #Constructor
    def __init__(self, radius:float = 1.0, color:str = "red"):
        self.__radius = radius
        self.__color = color
        return
    
    #Methods
    def getRadius(self) -> float:
        return self.__radius
    def setRadius(self, radius:float):
        self.__radius = radius
    def getColor(self) -> str:
        return self.__color
    def setColor(self, color:str):
        self.__color = color
    def __str__(self) -> str:
        return "circle of radius " + str(self.getRadius()) + " and color " + self.getColor()
    def getArea(self) -> float:
        return math.pi * self.getRadius()**2