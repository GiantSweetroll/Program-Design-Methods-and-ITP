import numpy as py
import random

words:() = ("Apple", "Windows", "Generate", "Password", "Bottle", "Charger", "Mouse")

def wantStrongPass() -> bool:
    print("How strong do you want your password to be?")
    print("1. Weak")
    print("2. Strong")
    response:str = input("Response: ")
    if response == "1" or response.casefold() == "weak".casefold():
        return False
    else:
        return True

def generatePassword(strongPass:bool) -> str:
    password:str = ""
    if strongPass:
        length:int = py.random.randint(12, 30)
        for _ in range(length):
            charType:int = py.random.randint(0, 4)
            if charType == 0:
                #lower case
                password += random.choice([chr(x) for x in range(97, 123)])
            elif charType == 1:
                #upper case
                password += random.choice([chr(x) for x in range(65, 91)])
            elif charType == 2:
                #Numbers
                password += random.choice([str(x) for x in range(0, 10)])
            elif charType == 3:
                #Symbols
                password += random.choice(["!", "@", "#", "%", "^", "&", "*", "_", "-"])
    else:
        for _ in range(2):
            password += random.choice(words)
    
    return password

print("Generated Password:", generatePassword(wantStrongPass()))
