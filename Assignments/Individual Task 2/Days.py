def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: " ))
    print("The number of days is:", round(get_days(hours, minutes, seconds), 4))
    return

def get_days(hours, minutes, seconds)->float:
    #convert to seconds
    allSeconds = hours*3600 + minutes*60 + seconds
    #Convert to days from all seconds
    return allSeconds/(3600*24)

convert_to_days()