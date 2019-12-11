import io
f = io.open("textbook.txt", encoding = "utf8")
contents = f.readlines()
f.close()

f2 = io.open("lined_textbook.txt", "a", encoding = "utf8")

i = 1

for content in contents:
    f2.write(str(i) + ". " + content)
    i+=1
f2.close()