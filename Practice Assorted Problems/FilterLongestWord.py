def filter_long_words(lwords:list, n:int)->list:
    array:list = []
    for word in lwords:
        if (len(word) > n):
            array.append(word)
    
    return array

print(filter_long_words(["Baba", "Yega", "Wick", "Neil", "Armstrong", "Judas"], 4))