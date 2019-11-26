E_EXCEPTIONS:tuple = ("be", "see", "flee", "knee")
VOWELS:tuple = ("a", "e", "i", "o", "u")

def verb_is_e_exception(verb:str)->bool:
    for suffix in E_EXCEPTIONS:
        if (verb.casefold() == suffix.casefold()):
            return True
    return False

def isVowel(letter:str)->bool:  #check if its vowel
    for vowel in VOWELS:
        if (vowel.casefold() == letter.casefold()):
            return True;

    return False

def consist_of_cvc(verb:str)->bool:
    
    return (not isVowel(verb[0]) and isVowel(verb[1]) and not isVowel(verb[-1]))
        

def makeForming(verb:str) -> str:
    if (verb_is_e_exception(verb)):
        verb = verb + "ing"
    elif (verb.endswith("ie")):
        verb = verb[0:-2] + "ying"
    elif (verb.endswith("e")):
        verb = verb[0:-1] + "ing"
    elif (consist_of_cvc(verb)):
        verb = verb + verb[-1] + "ing"
    else:
        verb = verb + "ing"
    
    return verb

verbs:tuple = ("lie", "see", "move", "hug")
for verb in verbs:
    print(makeForming(verb))
        