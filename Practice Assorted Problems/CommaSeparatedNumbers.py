string:str = input("Enter your numbers: ")

#List
numbersList:list = string.split(", ", -1)
print("List:", numbersList)

#Tuples
numbersTuple:tuple = tuple(numbersList)
print("Tuple:", numbersTuple)