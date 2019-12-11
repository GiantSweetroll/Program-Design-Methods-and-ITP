import io
import random


f = io.open("pokemonNames.txt")

contents = f.read()
f.close()

def getChain() -> [str]:
    #Separate to first letter dictionary
    names:[] = contents.split()
    firstNames:{} = {}
    
    for name in names:
        firstLetter:str = name[0:1]
        if firstLetter in firstNames:
            firstNames[firstLetter].append(name)
        else:
            firstNames[firstLetter] = [name]
    
    chain:[str] = []
    i:str = random.choice(list(firstNames.keys()))
    while(len(firstNames) != 0):
        try:
            ls = list(firstNames[i])
        except KeyError:
            break
        
        if len(ls) != 0:
            index = random.randint(0, len(ls)-1)
            
            name:str = ls[index]
            chain.append(name)
            
            del(firstNames[i][index])
            
            i = name[-1:]
        else:
            break
    return chain

for i in range(10):
    print(getChain())
