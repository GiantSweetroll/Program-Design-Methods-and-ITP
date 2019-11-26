def char_freq(string)->dict:
    
    freq:dict = {}
    
    for i in range(len(string)):
        letter:str = string[i:(i+1)]
        letter = letter.casefold()
        
        try:
            freq[letter] = int(str(freq[letter])) + 1
        except KeyError:
            freq[letter] = 1

    
    return freq

print(char_freq("Hello World"))