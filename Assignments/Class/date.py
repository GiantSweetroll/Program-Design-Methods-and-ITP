class Date():
    
    #Fields
    __day:int
    __month:int
    __year:int
    
    #Constructor
    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year
    
    #Methods
    getDay = lambda self: self.__day
    getMonth = lambda self: self.__month
    getYear = lambda self: self.__year
    def setDay(self, day:int):
        self.__day = day
    def setMonth(self, month:int):
        self.__month = month
    def setYear(self, year:int):
        self.__year = year
    def setDate(self, day:int, month:int, year:int):
        self.setDay(day)
        self.setMonth(month)
        self.setYear(year)
    def toString(self) ->str:
        mapped = list(map(lambda x: "0" + x if len(x)==1 else x, [str(self.getDay()), str(self.getMonth())]))
        return mapped[0] + "/" + mapped[1] + "/" + str(self.getYear())