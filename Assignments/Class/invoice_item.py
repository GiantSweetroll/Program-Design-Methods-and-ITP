class InvoiceItem():
    
    #Fields
    __id:str
    __desc:str
    __qty:int
    __unit_price = float
    
    #Constructor
    def __init__(self, invoiceID:str, desc:str, qty:int, unit_price: float):
        self.__id = invoiceID
        self.__desc = desc
        self.__qty = qty
        self.__unit_price = unit_price
    
    #Methods
    getID = lambda self: self.__id
    getDesc = lambda self: self.__desc
    getQty = lambda self: self.__qty
    getUnitPrice = lambda self: self.__unit_price
    getTotal = lambda self: self.getUnitPrice() * self.getQty()
    toString = lambda self: "InvoiceItem[id=" + self.getID() + ", desc=" + self.getDesc() + ", qty=" + str(self.getQty()) + ", unitPrice=" + str(self.getUnitPrice()) + "]"
    def setQty(self, qty:int):
        self.__qty = qty
    def setUnitPrice(self, unitPrice:float):
        self.__unit_price = unitPrice