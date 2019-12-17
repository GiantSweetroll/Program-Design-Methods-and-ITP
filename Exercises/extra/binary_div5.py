binaries:[] = input("Enter binaries: ").split(",")
filtered:[] = []

def convertToDecimal(binaryStr:str):
    binaryStr = binaryStr[::-1] #reverse
    result = 0
    counter = 0
    for digit in binaryStr:
        if digit == "1":
            result += 2**counter
        counter+=1
    
    return result

#Filtering divisible by 5
for binaryGroup in binaries:
    dec = convertToDecimal(binaryGroup)
    if dec%5==0:
        filtered.append(binaryGroup)

#Printing filtered binaries
for i in range(len(filtered)):
    print(filtered[i], end='')
    if i < len(filtered)-1:
        print(",", end='')