def mapLengths(words:list)->dict:
    dictionary:dict = {}
    for word in words:
        dictionary[word] = len(word)
        
    return dictionary

print(mapLengths(["Hello", "World"]))