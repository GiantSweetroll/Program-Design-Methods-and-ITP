invitation = ["Mike", "Brandon", "Alex"]
for i in range(len(invitation)):
    print("Hello " + invitation[i] + ", you are invited for dinner!")
    
print(invitation[0] + " cannot come")
del invitation[0]
invitation.insert(0, "Daniel")

for i in range(len(invitation)):
    print("Hello " + invitation[i] + ", you are invited for dinner!")
    
print("Guys, I found a bigger dining table!")
invitation.insert(0, "Audrey")
invitation.insert(2, "Mira")
invitation.append("Capitao")
for i in range(len(invitation)):
    print("Hello " + invitation[i] + ", you are invited for dinner!")
    
print("Sorry amigos, turns out I can only invite two of you lol")
for i in range(len(invitation)-2):
   print(invitation.pop(0) + ", I'm sorry but you're not invited anymore lmao") 

for i in range(len(invitation)):
    print("Hello " + invitation[i] + ", you are STILL invited for dinner!")
    
for i in range(len(invitation)):
    del(invitation[0])

print(invitation)
