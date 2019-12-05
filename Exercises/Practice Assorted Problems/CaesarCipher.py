def encode(msg:str, shift:int = 13)->str:
    charArray = []
    
    for i in range(len(msg)):
        letter:str = msg[i:(i+1)]
        #move by selected shift index
        index:int = ord(letter) + shift
        if (index > 127):
            index = index - 127 - 1 #First ASCII index is 0
        letter = chr(index)
        charArray.append(letter)
    
    encoded:str = ""
    encoded = encoded.join(charArray)
    return encoded

def decode(msg:str, shift:int = 13)->str:
    charArray = []
    
    for i in range(len(msg)):
        letter:str = msg[i:(i+1)]
        #move by selected shift index
        index:int = ord(letter) - shift
        if (index < 0):
            index = 127 - (index*-1 - 1) #First ASCII index is 0
        letter = chr(index)
        charArray.append(letter)
    
    decoded:str = ""
    decoded = decoded.join(charArray)
    return decoded

msg:str = "hello"
encoded:str = encode(msg, 13)
decoded:str = decode(encoded, 13)

print("Original Message:", msg)
print("Encoded Message:", encoded)
print("Decoded Message:", decoded)