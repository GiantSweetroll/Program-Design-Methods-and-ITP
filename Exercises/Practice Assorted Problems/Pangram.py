def generateCharacterDict()->dict:
    alphabet:dict = {}
    for i in range(65, 91, 1):
        string:str = str(chr(i))
        alphabet[string.casefold()] = 0
    
    return alphabet

def isPangram(sentence:str)->bool:
    alphabet:dict = generateCharacterDict()
    
    for i in range(len(sentence)):
        letter:str = sentence[i:(i+1)]
        if (letter == " "):
            continue
        
        alphabet[letter.casefold()] = int(str(alphabet[letter.casefold()])) + 1
    
    for i in alphabet:
        if (alphabet[i] == 0):
            return False
    
    return True

print(isPangram("The quick brown fox jumps over the lazy dog"))