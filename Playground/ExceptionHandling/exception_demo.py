names = ["Nico", "Bently", "Jason"]

try:
    print(names[0])
    print(names[1])
    print(names[2])
    names[2] += 2
except IndexError:
    print("Exception was found")
except:
    print("Other error")
print("Hello")