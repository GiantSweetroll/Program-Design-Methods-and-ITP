from Assignments.OOP.Circle.circle import Circle

class Cylinder(Circle):
    
    #Fields
    __height:float
    
    #Constructor
    def __init__(self, height:float = 1.0, radius:float = 1.0, color:str = "red"):
        super().__init__(radius, color)
        self.__height = height
    
    #Methods
    def getHeight(self) -> float:
        return self.__height
    def setHeight(self, height:float):
        self.__height = height
    def __str__(self)->str:
        return "Cylinder of height " + str(self.getHeight()) + ", radius " + str(self.getRadius()) + ", and color " + self.getColor()
    def getVolume(self) -> float:
        return self.getArea() * self.getHeight()