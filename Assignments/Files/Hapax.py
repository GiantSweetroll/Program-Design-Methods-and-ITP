import io
class Hapax():
    
    #Fields
    listings:{}
    
    #Constructor
    def __init__(self):
        self.listings = {}
        
        f = io.open("textbook.txt", encoding="utf8")
        if f.mode == 'r':
            contents = f.readlines()
            for x in contents:
                substrings = x.split()
                for substring in substrings:
                    #print(substring,":", substring[-1:len(substring)], "->", substring[0:-1])
                    if substring[-1:] in [",", ".", "?", "!", ":", ";", "\"", "\'", ")", "]"]:
                        substring = substring[0:-1]
                    if substring[0:1] in ["\"", "\'", "(", "["]:
                        substring = substring[1:]
                        
                    if substring in self.listings:
                        self.listings[substring.casefold()] += 1
                    else:
                        self.listings[substring.casefold()] = 1
            f.close()
    
    #Methods
    def getHapaxList(self) -> [str]:
        hapax = []
        for word in self.listings:
            if self.listings[word] == 1:
                hapax.append(word)
        return hapax

hapax:Hapax = Hapax()
hapx = hapax.getHapaxList()
for word in hapx:
    try:
        print(word)
    except UnicodeEncodeError:
        continue