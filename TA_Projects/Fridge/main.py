from TA_Projects.Fridge.fridge_part.fridge import Fridge
import os
from TA_Projects.Fridge.item.item import Item
from TA_Projects.Fridge.item.food import Food
from TA_Projects.Fridge.item.beverage import Beverage
from TA_Projects.Fridge.item.non_edible import NonEdible
from TA_Projects.Fridge.container.container import Container

fridge:Fridge = Fridge()
foodList:() = (Food.DAIRY, 
               Food.EGG, 
               Food.FRUIT, 
               Food.GRAIN, 
               Food.ICE_CREAM, 
               Food.ICE_CUBE, 
               Food.JELLY, 
               Food.MEAT, 
               Food.PUDDING, 
               Food.SOUP)
bevList:() = (Beverage.ALCOHOL,
              Beverage.COFFEE,
              Beverage.JUICE,
              Beverage.MILK,
              Beverage.SYRUP,
              Beverage.TEA,
              Beverage.WATER)
nonEdiList:() = (NonEdible.CHAIR,
                 NonEdible.LAPTOP,
                 NonEdible.POWER_GLUE,
                 NonEdible.RADIO)

def clear():
    os.system('cls')

def printWelcomeScreen() -> int:
    print("Hello, do you want to use your fridge?")
    print("1. Yes")
    print("2. No")
    response:str = input("Response: ")
    if response == "1" or response.casefold() == "yes".casefold():
        return 1
    elif response=="2" or response.casefold() == "no".casefold():
        return 2
    else:
        print("Invalid input, please try again.")
        return -1

def printFridgeActionSelection() -> int:
    print("What do you want to do?")
    print("1. Store")
    print("2. Take")
    print("3. View")
    print("4. Clear Fridge")
    print("5. Exit")
    response:str = input("Response: ")
    if response == "1" or response.casefold() == "store".casefold():
        return 1
    elif response == "2" or response.casefold() == "take".casefold():
        return 2
    elif response == "3" or response.casefold() == "view".casefold():
        return 3
    elif response == "4" or response.casefold() == "clear fridge".casefold():
        return 4
    elif response == "5" or response.casefold() == "exit".casefold():
        return 5
    else:
        print("Invalid input, please try again.")
        return -1

def printFridgeSectionSelection() -> int:
    print("Select part of the fridge")
    print("1.", fridge.freezer.getName())
    print("2.", fridge.body.getName())
    response:str = input("Response: ")
    if response == "1" or response.casefold() == fridge.freezer.getName().casefold():
        return 1
    elif response == "2" or response.casefold() == fridge.body.getName().casefold():
        return 2
    else:
        print("Invalid input, please try again.")
        return -1

def printItemClassSelection(text:str) -> int:
    print(text)
    print("1. Food")
    print("2. Beverages")
    print("3. Non-edibles")
    response:str = input("Response: ")
    if response == "1" or response.casefold() == "Food".casefold():
        return 1
    elif response == "2" or response.casefold() == "Beverages".casefold():
        return 2
    elif response == "3" or response.casefold() == "Non-edibles".casefold():
        return 3
    else:
        print("Invalid input, please try again.")
        return -1

def printFoodTypeSelection() -> int:
    print("Select what kind of Food")
    i = 0
    arrLen:int = len(foodList)
    for i in range(arrLen):
        print(str(i+1) + ".", foodList[i])
    print(str(arrLen+1) + ".", "Other")
    response:str = input("Response: ")
    for a in range(arrLen):
        if (int(response)-1)==a or response.casefold() == foodList[a].casefold():
            return a
    if response == str(arrLen+1) or response.casefold() == "Other".casefold():
        return arrLen+1
    else:
        print("Invalid input, please try again.")
        return -1

def printBeveragesTypeSelection() -> int:
    print("Select what kind of Beverages")
    i = 0
    arrLen:int = len(bevList)
    for i in range(arrLen):
        print(str(i+1) + ".", bevList[i])
    print(str(arrLen+1) + ".", "Other")
    response:str = input("Response: ")
    for a in range(arrLen):
        if (int(response)-1)==a or response.casefold() == bevList[a].casefold():
            return a
    if response == str(arrLen+1) or response.casefold() == "Other".casefold():
        return arrLen+1
    else:
        print("Invalid input, please try again.")
        return -1

def printNonEdibleTypeSelection() -> int:
    print("Select what kind of Non-Edibles")
    i = 0
    arrLen:int = len(nonEdiList)
    for i in range(arrLen):
        print(str(i+1) + ".", nonEdiList[i])
    print(str(arrLen+1) + ".", "Other")
    response:str = input("Response: ")
    for a in range(arrLen):
        if (int(response)-1)==a or response.casefold() == nonEdiList[a].casefold():
            return a
    if response == str(arrLen+1) or response.casefold() == "Other".casefold():
        return arrLen+1
    else:
        print("Invalid input, please try again.")
        return -1

def printItemInitializer(itemClass:str, itemType:str) -> Item:
    itemName:str = input("Enter " + itemClass + " item name: ")
    amount:int = 0
    while(amount <= 0):
        try:
            amount = int(input("Enter amount: "))
            if amount <=0:
                print("Invalid input, please try again.")
        except:
            print("Invalid input, please try again.")
            amount = 0
    if itemClass == "Food":
        return Food(itemName, amount, itemType)
    elif itemClass == "Beverage":
        return Beverage(itemName, amount, itemType)
    else:
        return NonEdible(itemName, amount, itemType)

def printItemMaker(itemClassSelText:str) -> Item:
    itemClass:int = -1
    while(itemClass == -1):
        itemClass = printItemClassSelection(itemClassSelText)
    if itemClass == 1: #Food
        foodType:int = -1
        while(foodType == -1):
            try:
                foodType = foodList[printFoodTypeSelection()]
            except:
                foodType = "Other"
        return printItemInitializer("Food", foodType)
    elif itemClass == 2: #Beverages
        bevType:int = -1
        while(bevType == -1):
            try:
                bevType = bevList[printBeveragesTypeSelection()]
            except:
                bevType = "Other"
        return printItemInitializer("Beverage", bevType)
    elif itemClass == 3: #Non-Edible
        nonEdiType:int = -1
        while(nonEdiType == -1):
            try:
                nonEdiType = nonEdiList[printNonEdibleTypeSelection()]
            except:
                nonEdiType = "Other"
        return printItemInitializer("Non-Edible", nonEdiType)

def printFreezerContainersSelection() -> int:
    print("Select freezer container")
    arrLen:int = len(fridge.freezer.containers)
    for i in range(arrLen):
        print(str(i+1) + ".", fridge.freezer.containers[i].getName(), " (" + str(fridge.freezer.containers[i].getSpaceLeft()) + " space left)")
    response:str = input("Response: ")
    for i in range(arrLen):
        if (int(response)-1) == i or response.casefold() == fridge.freezer.containers[i].getName():
            return i
    print("Invalid input, please try again.")
    return -1

def printMainFridgeContainersSelection() -> int:
    print("Select main fridge container")
    arrLen:int = len(fridge.body.containers)
    for i in range(arrLen):
        print(str(i+1) + ".", fridge.body.containers[i].getName(), " (" + str(fridge.body.containers[i].getSpaceLeft()) + " space left)")
    response:str = input("Response: ")
    for i in range(arrLen):
        if (int(response)-1) == i or response.casefold() == fridge.body.containers[i].getName():
            return i
    print("Invalid input, please try again.")
    return -1

def storeItem(container:Container, item:Item):
    if container.getSpaceLeft() > item.getSize():
        container.store(item, item.getSize())
        print(item.getName(), "was stored.")
    else:
        print(item.getName(), "was not stored due to not enough space in the", container.getName(), "container")

def printTakeItemSelection(container:Container):
    while(True):
        print("Items stored in", container.getName())
        listItemsStoredInContainer(container, True)
        print("What would you like to take? Type \"-1\" to cancel")
        response:str = input("Response: ")
        if response == "\"-1\"" or response == "-1":
            return
        itemList:{} = container.getItemsList()
        i:int = 1
        for itemClass in itemList:
            for itemType in itemList[itemClass]:
                for itemName in itemList[itemClass][itemType]:
                    if response == str(i) or response == itemName.casefold():
                        #How much to take
                        amount:int = -1
                        while(amount == -1):
                            try:
                                amount = int(input("How much " + itemName + " would you like to take?: "))
                                if amount < 0 or amount > itemList[itemClass][itemType][itemName]:
                                    amount = -1
                                    print("Invalid input, please try again.")
                            except:
                                amount = -1
                                print("Invalid input, please try again.")
                        #reduce item
                        itemList[itemClass][itemType][itemName] -= amount
                        print(amount, "pieces of", itemName, "was removed from", container.getName(), "container")
                        #if empty, delete data entry in dictionary
                        if itemList[itemClass][itemType][itemName] == 0:
                            del(itemList[itemClass][itemType][itemName])
                            if len(itemList[itemClass][itemType]) == 0:
                                del(itemList[itemClass][itemType])
                                if len(itemList[itemClass]) == 0:
                                    del(itemList[itemClass])
                        return
                    i+=1
        print("Invalid input, please try again.")

def listItemsStoredInContainer(container:Container, showNumbers:bool, indent:str = ""):
    if showNumbers:
        itemList:{} = container.getItemsList()
        i:int = 1
        for itemClass in itemList:
            print(indent + itemClass + ":")
            for itemType in itemList[itemClass]:
                print(indent + "    " + itemType + ":")
                for itemName in itemList[itemClass][itemType]:
                    print(indent + "        " + str(i) + ". " + itemName + ":", itemList[itemClass][itemType][itemName])
                    i+=1
    else:
        itemList:{} = container.getItemsList()
        for itemClass in itemList:
            print(indent + itemClass + ":")
            for itemType in itemList[itemClass]:
                print(indent + "    " + itemType + ":")
                for itemName in itemList[itemClass][itemType]:
                    print(indent + "        " + itemName + ":", itemList[itemClass][itemType][itemName])

def viewItemsInFridge():
    print("Freezer:")
    for container in fridge.freezer.containers:
        print("    " + container.getName())
        listItemsStoredInContainer(container, False, "        ")
    print("Main Fridge:")
    for container in fridge.body.containers:
        print("    " + container.getName())
        listItemsStoredInContainer(container, False, "        ")
        
def printClearFridgeSelection() -> int:
    print("Are you sure you want to clear your fridge?")
    print("1. Yes")
    print("2. No")
    response:str = input("Response: ")
    if response == "1" or response.casefold() == "Yes".casefold():
        return 1
    elif response == "2" or response.casefold() == "No".casefold():
        return 2
    else:
        print("Invalid input, please try again")
        return -1

def clearFridge():
    for container in fridge.freezer.containers:
        container.clear()
    for container in fridge.body.containers:
        container.clear()

#Main
def main():
    while(True):
        response:int = -1
        #Open fridge
        while(response == -1):
            response:int = printWelcomeScreen()
        if response == 2:
            break
        else:
            #what to do with fridge
            response = -1
            while(response == -1):
                response = printFridgeActionSelection()
            if response == 5:
                return
            elif response == 1: #Insert things into the fridge
                item:Item = printItemMaker("Select what kind of item you want to store?")
                response = -1
                while(response == -1):
                    #fridge section selection
                    response = printFridgeSectionSelection()
                fridgeSelection:int = response
                if fridgeSelection == 1: #if freezer
                    response = -1
                    while (response == -1):
                        response = printFreezerContainersSelection()
                    container:int = response
                    #put item into container
                    storeItem(fridge.freezer.containers[container], item)
                elif fridgeSelection == 2: #If body
                    response = -1
                    while (response == -1):
                        response = printMainFridgeContainersSelection()
                    container:int = response
                    #put item into container
                    storeItem(fridge.body.containers[container], item)
            elif response == 2: #Take things from fridge
                response = -1
                while(response == -1):
                    #fridge section selection
                    response = printFridgeSectionSelection()
                fridgeSelection:int = response
                if fridgeSelection == 1: #if freezer
                    response = -1
                    while (response == -1):
                        response = printFreezerContainersSelection()
                    container:int = response
                    #take item into container
                    printTakeItemSelection(fridge.freezer.containers[container])
                elif fridgeSelection == 2: #If body
                    response = -1
                    while (response == -1):
                        response = printMainFridgeContainersSelection()
                    container:int = response
                    #take item into container
                    printTakeItemSelection(fridge.body.containers[container])
            elif response == 3: #View Fridge
                viewItemsInFridge()
            elif response ==4: #Clear fridge
                response = -1
                while(response == -1):
                    response = printClearFridgeSelection()
                if response == 1:
                    clearFridge()
                    print("Fridge has been cleared")
            else:
                print("Invalid input, please try again.")

main()
    