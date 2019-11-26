ES_SUFFIXES = ("o","ch", "s", "sh", "x", "z")

def es_suffix_possible(verb:str)->bool:
    for suffix in ES_SUFFIXES:
        if (verb.endswith(suffix)):
            return True
        
    return False

def makeForms(verb:str)->str:
    charArray = []
    
    for i in range(len(verb)):
        letter:str = verb[i:(i+1)]
        charArray.append(letter)
    
    if (verb.endswith("y")):
        charArray[-1] = "ies"
    elif (es_suffix_possible(verb)):
        charArray.append("es")
    else:
        charArray.append("s")
    
    verb = ""
    verb = verb.join(charArray)
    
    return verb

verbs = ("try", "brush", "run", "fix")
for verb in verbs:
    print(makeForms(verb))