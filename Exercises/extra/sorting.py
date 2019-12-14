import io
f = io.open("names_for_sorting.txt", encoding = "utf8")
names = f.read().splitlines()
ls:[] = []

#Init items
for name in names:
    ls.append(tuple(name.split(",")))
f.close()

#Sorting
def sortName(listIndex1, listIndex2, index, maks):
    if index < maks:
        letter1 = (ls[listIndex1][0].casefold())[index:index+1]
        letter2 = (ls[listIndex2][0].casefold())[index:index+1]
        if letter1 > letter2:
            temp = ls[listIndex1]
            ls[listIndex1] = ls[listIndex2]
            ls[listIndex2] = temp
        elif letter1 == letter2:
            sortName(listIndex1, listIndex2, index+1, maks)
        else:
            pass
    else:
        #put the one with lesser character first
        if len(ls[listIndex1][0]) > len(ls[listIndex2][0]):
            temp = ls[listIndex1]
            ls[listIndex1] = ls[listIndex2]
            ls[listIndex2] = temp
            
for i in range(len(ls)-1):
    for a in range(i+1, len(ls)):
        sortName(i, a, 0, len(ls[i][0]) if len(ls[i][0]) < len(ls[a][0]) else len(ls[a][0]))
    for a in range(i+1, len(ls)):
        if ls[i][0] == ls[a][0]:
            if ls[i][1] > ls[a][1]:
                temp = ls[i]
                ls[i] = ls[a]
                ls[a] = temp
    for a in range(i+1, len(ls)):
        if ls[i][0] == ls[a][0]:
            if ls[i][1] == ls[a][1]:
                if ls[i][2] > ls[a][2]:
                    temp = ls[i]
                    ls[i] = ls[a]
                    ls[a] = temp

print(ls)
