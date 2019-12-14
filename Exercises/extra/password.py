upperCase:[] = [chr(x) for x in range(65, 91)]
lowerCase:[] = [chr(x) for x in range(97, 123)]
numbers:[] = [str(x) for x in range(0, 10)]
specials:[] = ["$", "#", "@"]
minChar = 6
maxChar = 12

passwords:[] = (input("Enter your passwords: ")).split(",", -1)

for password in passwords:
    checking:[] = [0, 0, 0, 0]
    for letter in password:
        if letter in specials:
            checking[0]+=1
        elif letter in numbers:
            checking[1]+=1
        elif letter in upperCase:
            checking[2]+=1
        elif letter in lowerCase:
            checking[3]+=1
    if 0 not in checking:
        length = len(password)
        if length >= 6 and length <= 12:
            print(password)