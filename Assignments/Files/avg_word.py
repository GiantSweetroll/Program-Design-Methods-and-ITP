import io

f = io.open("textbook.txt", encoding="utf8")

contents = f.readlines()

f.close()

wordsLengthTotal = 0
words = 0

for content in contents:
    substrings = content.split()
    for substring in substrings:
        #print(substring,":", substring[-1:len(substring)], "->", substring[0:-1])
        if substring[-1:] in [",", ".", "?", "!", ":", ";", "\"", "\'", ")", "]"]:
            substring = substring[0:-1]
        if substring[0:1] in ["\"", "\'", "(", "["]:
            substring = substring[1:]
        
        wordsLengthTotal += len(substring)
        words += 1

print("Average word length: ", wordsLengthTotal//words)