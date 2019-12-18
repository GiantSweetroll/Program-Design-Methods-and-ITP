from quiz.part_ii.q2 import Methods
from quiz.part_ii.q2.staff import Staff


class Menu():
    
    #Fields
    staffList:[]
    
    #Constructor
    def __init__(self, staff:[]):
        self.staffList = staff
        self.menu(self.staffList)
    
    #Methods
    def displayRecords(self, staff:[Staff]):
        print("|ID    |Name        |Position        |Salary        |")
        for stf in staff:
            print("|" + stf.staffID + "  |" + stf.name + "       |" + stf.position + "        |" + str(stf.salary))
    
    def displayRecordsAndOptions(self, staff:[Staff]):
        self.displayRecords(staff)
        print("1. New Staff")
        print("2. Delete Staff")
        print("3. View Summary Data")
        print("4. Save & Exit")
        
    def getMaxMinAvgSalary(self, staffList):
        maxim = 0
        minim = staffList[0].salary
        total = 0
        for staff in staffList:
            salary = staff.salary
            total += salary
            if salary > maxim:
                maxim = salary
            if salary < minim:
                minim = salary
        
        return [minim, maxim, total//len(staffList)]
    def getPositionList(self, staffList):
        positions = {}
        for staff in staffList:
            if staff.position in positions:
                positions[staff.position].append(staff)
            else:
                positions[staff.position] = [staff]
        
        return positions
    
    def menu(self, staffList: []):
        ids = [x.staffID for x in staffList]
        self.displayRecordsAndOptions(staffList)
        response:str = input("Input Choice: ")
        
        if response == str("1") or response.casefold() == "New Staff".casefold():
            #New Staff
            print("New Staff")
            staffID:str = ""
            while(True):
                staffID = input("Input Staff ID[SXXXX]: ")
                if len(staffID) != 5 or staffID[:1] != "S":
                    continue
                else:
                    if staffID in ids:
                        continue
                    
                    for i in range(1, len(staffID)):
                        if staffID[i:i+1] not in [x for x in range(10)]:
                            continue
                    break
            name:str = ""
            while(True):
                name = input("Input name[0...20]: ")
                if len(name) > 20:
                    continue
                break
            
            position:str = ""
            while(True):
                position = input("Input Position [Staff|Officer|Manager]: ")
                if position.casefold() not in ["staff", "officer", "manager"]:
                    continue
                break
            
            salary:int = 0
            while(True):
                salary = int(input("Input Salary for " + position +": "))
                if position.casefold() == "Staff".casefold():
                    if salary<3500000 or salary > 7000000:
                        continue
                elif position.casefold() == "Officer".casefold():
                    if salary<7000001 or salary > 10000000:
                        continue
                elif position.casefold() == "Manager".casefold():
                    if salary <= 10000000:
                        continue
                break
            newStaff = Staff(staffID, name, position, salary)
            self.staffList.append(newStaff)
            Methods.sortStaffByName(self.staffList)
            self.menu(self.staffList)
        elif response == "2" or response.casefold() == "Delete Staff".casefold():
            #Delete Staff
            print("Delete Staff")
            staffID:str = input("Input ID[SXXXX]: ")
            if staffID in ids:
                for i in range(len(self.staffList)):
                    if self.staffList[i].staffID == staffID:
                        del(self.staffList[i])
                        break
                print("Data has been successfully deleted")
            else:
                print("Data not found")
            self.menu(self.staffList)
        elif response == "3" or response.casefold() == "View summary data".casefold():
            #View Summary Data
            positions = self.getPositionList(self.staffList)
            i = 1
            for  position in positions:
                print(str(i) + ".", position)
                ls = self.getMaxMinAvgSalary(positions[position])
                print("Minimum Salary:", ls[0])
                print("Maximum Salary:", ls[1])
                print("Average Salary:", ls[2])
                print()
            self.menu(self.staffList)
        elif response == "4" or response.casefold() == "Save & Exit".casefold():
            #Save and exit
            Methods.sortStaffByName(self.staffList)
            with open("data.txt", "w") as f:
                for staff in self.staffList:
                    f.write(staff.__str__() + "\n")
        else:
            self.menu(staffList)
    