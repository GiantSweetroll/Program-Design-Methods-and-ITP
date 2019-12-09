class Employee():
    #Fields
    __id:int
    __firstName:str
    __lastName:str
    __salary:int
    
    #Constructor
    def __init__(self, employeeID:int, firstName:str, lastName:str, salary:int):
        self.__id = employeeID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__salary = salary
        
    #Methods
    getID:str = lambda self: self.__id
    getLastName:str = lambda self: self.__lastName
    getFirstName:str = lambda self: self.__firstName
    getName:str = lambda self: self.__firstName + " " + self.__lastName
    getSalary:int = lambda self: self.__salary
    getAnnualSalary = lambda self: self.__salary * 12
    def setSalary(self, amount:int):
        self.__salary = amount
    def raiseSalary(self, percent:int) -> int:
        newSalary:int = int(self.getSalary * percent/100)
        self.setSalary(newSalary)
        return self.getSalary
    def __str__(self) -> str:
        return "Employee[id=" + self.getID() + ", name=" + self.getName() + ", salary=" + self.getSalary() + "]"
    