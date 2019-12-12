import io

f = io.open("sentence.txt", encoding="utf8")
contents = f.read()

digits:[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sentences:[] = []
titles:[str] = ["Mr.", "Ms.", "Mrs.", "Dr."]
punctuations:[str] = [".", "!", "?"]

#Split all spaces regardless
words:[str] = contents.split()

#Checking
def conjoint(arr:[], begin:int, end:int) -> str:
    words:str = ""
    for i in range(begin, end+1):
        words += arr[i] + " "
    return words

begin:int = 0
end:int = 0
while len(words) > 0:
    #Check if title
    if words[end] in titles:
        end+=1
        continue
    
    #Check for punctuations
    if words[end][-3:] == "...":
        try:
            #check next word if lowercase
            if words[end+1] != words[end+1].capitalize():   #lower case
                end+=1
            else:
                #Capital, so it's a sentence breaker
                sentences.append(conjoint(words, begin, end))
                for _ in range(begin, end+1):
                    del(words[begin])
                end = 0 
            continue
        except IndexError:
            sentences.append(conjoint(words, begin, end))
            for _ in range(begin, end+1):
                del(words[begin])
            break
    elif words[end][-1:] in punctuations:
        try:
            #check next word if lowercase
            if words[end+1] != words[end+1].capitalize():   #lower case
                end+=1
            else:
                #Capital, so it's a sentence breaker
                sentences.append(conjoint(words, begin, end))
                for _ in range(begin, end+1):
                    del(words[begin])
                end = 0 
            continue
        except IndexError:
            sentences.append(conjoint(words, begin, end))
            for _ in range(begin, end+1):
                del(words[begin])
            break
    end+=1
    
for sentence in sentences:
    print(sentence)