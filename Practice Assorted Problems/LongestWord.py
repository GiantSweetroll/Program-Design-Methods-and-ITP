def find_longest_word(lwords:list)->str:
    dictionary:dict = mapLengths(lwords)
    
    max:int = 0
    for num in dictionary:  #Find highest key
        if (num > max):
            max = num
    
    return dictionary[max]

def mapLengths(words:list)->dict:
    dictionary:dict = {}
    for word in words:
        dictionary[len(word)] = word
        
    return dictionary

print(find_longest_word(["Words", "To", "Live", "By"]))