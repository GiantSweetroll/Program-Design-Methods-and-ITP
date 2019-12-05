VOWELS:tuple = ("a", "e", "i", "o", "u")

def isVowel(letter:str)->bool:  #check if its vowel
    for vowel in VOWELS:
        if (vowel.casefold() == letter.casefold()):
            return True;

    return False

def getStringChunks(string:str)->list:
    charArray:list = []
    #substring
    for i in range(len(string)):
        charArray.append(string[i:(i+1)])
    
    return charArray

def translate(text):
    array:list = getStringChunks(text)
    array2:list = []
    
    for letter in array:
        if (isVowel(letter) or letter == " "):
            array2.append(letter)
        else:
            array2.append(letter)
            array2.append("o")
            array2.append(letter)
    
    #Convert array to string
    newWord:str = ""
    for letter in array2:
        newWord += letter
    
    print(newWord)
    return

translate("this is fun")