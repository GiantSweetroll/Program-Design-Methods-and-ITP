def convert_temp():
    farenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = convert_to_celsius(farenheit)
    
    print("The temperature in Fahrenheit is:", farenheit)
    print("The temperature in Celsius is:", celsius)
    print("The temperature in Kelvin is:", convert_to_kelvin(celsius))
    
def convert_to_celsius(tempF)->float:
    return (5/9)*(tempF-32)
t
def convert_to_kelvin(tempC)->float:
    return tempC + 273.15
    
convert_temp()