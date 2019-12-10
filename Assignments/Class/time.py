class Time():
    
    #Fields
    __hour:int
    __minute:int
    __second:int
    
    #Constructor
    def __init__(self, hour:int, minute:int, second:int):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    #Methods
    getHour = lambda self: self.__hour
    getMinute = lambda self:self.__minute
    getSecond = lambda self: self.__second
    def setHour(self, hour:int):
        self.__hour = hour
    def setMinute(self, minute:int):
        self.__minute = minute
    def setSecond(self, second:int):
        self.__second = second
    def setTime(self, hour:int, minute:int, second:int):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)
    def toString(self) -> str:
        mapped = list(map(lambda x: "0" + x if len(x)==1 else x, [str(self.getHour()), str(self.getMinute()), str(self.getSecond())]))
        return mapped[0] + ":" + mapped[1] + ":" + mapped[2]
    def nextSecond(self):
        second:int = self.getSecond() + 1
        minute:int = self.getMinute()
        hour:int = self.getHour()
        if second == 60:
            second = 0
            minute += 1
        
        if minute == 60:
            minute = 0
            hour += 1
        
        return Time(hour, minute, second)
    def previousSecond(self):
        second:int = self.getSecond() - 1
        minute:int = self.getMinute()
        hour:int = self.getHour()
        if second < 0:
            second = 59
            minute -= 1
        
        if minute < 0:
            minute = 59
            hour -= 1
        
        return Time(hour, minute, second)