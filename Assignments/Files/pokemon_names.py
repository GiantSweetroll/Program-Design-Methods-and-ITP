import copy
import io
import time


f = io.open("pokemonNames.txt")

contents = f.read()
f.close()

names:[] = contents.split()
firstNames:{} = {}
mutableFirstNames:{} = {}
allCombinations:[] = []

def createFirstLetterDictionary():
    for name in names:
        firstLetter:str = name[0:1]
        if firstLetter in firstNames:
            firstNames[firstLetter].append(name)
        else:
            firstNames[firstLetter] = [name]

def addChainToAllCombinationsList(chain):
    allCombinations.append(chain.split())
def getPokemonNameList(firstLetter:str, index:int, currentChain, remainingNames:{}):
    if firstLetter in remainingNames and index < len(remainingNames[firstLetter]):
        name:str = remainingNames[firstLetter][index]
        copyRemNames:{} = copy.deepcopy(remainingNames)
        del(copyRemNames[firstLetter][index])
        currentChain += " " + name
        firstLetter = name[-1:]
###         print(currentChain)
        if firstLetter not in copyRemNames:
#             print(firstLetter, "not in dictionary 1")
            addChainToAllCombinationsList(currentChain)
        else:
            length:int = len(copyRemNames[firstLetter])
            if length > 0:
                for i in range(length):
                    getPokemonNameList(firstLetter, i, currentChain, copyRemNames)
            else:
#                 print("length is 0")
                addChainToAllCombinationsList(currentChain)    
    else:
#         print(firstLetter, "not in dictionary 2")
        addChainToAllCombinationsList(currentChain)  

#Start
startTime = time.time()
createFirstLetterDictionary()
mutableFirstNames = firstNames
for letter in firstNames:
    for i in range(len(firstNames[letter])):
        getPokemonNameList(letter, i, "", mutableFirstNames)

#Find longest chain
index:int = 0
highest: int = 0
for i in range(len(allCombinations)):
    if len(allCombinations[i]) > highest:
        highest = len(allCombinations[i])
        index = i

#Print longest chain
print("Longest chain:", highest)
for name in allCombinations[index]:
    print(name)
print(startTime - time.time())