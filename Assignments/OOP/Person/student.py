from Assignments.OOP.Person.person import Person
class Student(Person):
    
    #Fields
    __numCourses:int
    __courses:[str]
    __grades:[int]
    
    #Constructor
    def __init__(self, name:str, address:str):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []
    
    #Methods
    def addCourseGrade(self, course:str, grade:int):
        self.__courses.append(course)
        self.__grades.append(grade)
    def printGrades(self):
        print("Grades:")
        for i in range(len(self.__courses)):
            print(self.__courses[i], ":", self.__grades[i])
    def getAverageGrade(self) -> float:
        total = 0
        for grade in self.__grades:
            total += grade
        return total / len(self.__grades)
    def __str__(self):
        return "Student: " + super().__str__()