from TA_Projects.Fridge.fridge_part.fridge import Fridge

fridge:Fridge = Fridge()

def printWelcomeScreen() -> int:
    print("Hello, do you want to use your fridge?")
    print("1. Yes")
    print("2. No")
    response = input("Response: ")
    if response == "1" or response=="2":
        return int(response)
    else:
        print("Invalid input, please try again.")
        return -1

#Main
while(True):
    