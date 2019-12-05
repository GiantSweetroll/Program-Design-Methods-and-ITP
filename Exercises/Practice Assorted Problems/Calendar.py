import calendar

def printCalendar(year:int):
    for i in range(12):
        print(calendar.month(year, i+1))
    return

printCalendar(2019)