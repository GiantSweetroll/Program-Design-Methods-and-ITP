from Assignments.OOP.Person.person import Person
class Teacher(Person):
    
    #Fields
    __numCourses:int
    __courses:[str]
    
    #Constructor
    def __init__(self, name:str, address:str):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
    
    #Methods
    def addCourse(self, course:str) -> bool:
        if course in self.__courses:
            return False
        else:
            self.__numCourses += 1
            self.__courses.append(course)
            return True
    def removeCourse(self, course:str) -> bool:
        for i in range(len(self.__courses)):
            if self.__courses[i] == course:
                del(self.__courses[i])
                return True
        
        return False
    def __str__(self)->str:
        return "Teacher: " + super().__str__()