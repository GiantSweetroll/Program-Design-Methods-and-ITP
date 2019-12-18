class Staff():
    def __init__(self, staffID, name, position, salary):
        self.staffID = staffID
        self.name = name
        self.position = position
        self.salary = int(salary)
    
    def __str__(self):
        return self.staffID+"#"+self.name+"#"+self.position+"#"+str(self.salary)