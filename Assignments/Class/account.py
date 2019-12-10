class Account():
    
    #Fields
    __id:str
    __name:str
    __balance:int
    
    #Constructor
    def __init__(self, accID:str, name:str, balance:int = 0):
        self.__id = accID
        self.__name = name
        self.__balance = balance
    
    #Methods
    getID = lambda self: self.__id
    getName = lambda self: self.__name
    getBalance = lambda self: self.__balance
    toString = lambda self: "Account[id=" + self.getID() + ", name=" + self.getName() + ", balace=" + str(self.getBalance()) + "]"
    def credit(self, amount:int) -> int:
        self.__balance += amount
        return self.getBalance()
    def debit(self, amount:int) -> int:
        if (amount <= self.getBalance()):
            self.__balance -= amount
        else:
            print("Amount exceed balance")
        return self.getBalance()
    def transferTo(self, another, amount:int) -> int:
        if (amount <= self.getBalance()):
            balance = another.getBalance()
            balance += amount
        else:
            print("Amount exceeds balance")
        return self.getBalance()