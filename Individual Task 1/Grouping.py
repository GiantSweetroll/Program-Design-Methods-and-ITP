classStudents = [32, 45, 51]

groups = [5, 7, 6]

def getLeftOver(students:int, groups:int)-> int:
    return students%groups

print("Number of students in each group:")
for i in range(len(groups)):
    print("Class", i+1, ":", int(classStudents[i]/groups[i]))
print()
print("Number of students leftover:")
for i in range(len(groups)):
    print("Class", i+1, ":", getLeftOver(classStudents[i], groups[i]))