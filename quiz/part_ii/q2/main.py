from quiz.part_ii.q2.staff import Staff
from quiz.part_ii.q2.Menu import Menu
from quiz.part_ii.q2 import Methods

def init_data_txt():
    with open("data.txt", "w") as f:
        f.write(Staff("S0001", "Garry", "Staff", "4500000").__str__() + "\n")
        f.write(Staff("S0002", "Larry", "Staff", "4500000").__str__() + "\n")
        f.write(Staff("S0003", "Mary", "Staff", "4500000").__str__() + "\n")
        f.write(Staff("S0004", "Susan", "Officer", "9500000").__str__() + "\n")
        f.write(Staff("S0005", "Bob", "Staff", "4500000").__str__() + "\n")
        f.write(Staff("S0006", "Bobby", "Staff", "4500000").__str__() + "\n")
        f.write(Staff("S0007", "George", "Staff", "4500000").__str__() + "\n")
        f.write(Staff("S0008", "Lina", "Manager", "119500000").__str__() + "\n")
        f.write(Staff("S0009", "Monty", "Staff", "4500000").__str__() + "\n")
        f.write(Staff("S0010", "Castle", "Staff", "4500000").__str__() + "\n")

def read_file():
    staff = []
    with open("data.txt") as f:
        data = f.readlines()
        for dt in data:
            staff.append(dt.split("#"))
    staffList = []
    for stf in staff:
        staffList.append(Staff(stf[0], stf[1], stf[2], stf[3]))
    return staffList

init_data_txt()
staffList:[] = read_file()
Methods.sortStaffByName(staffList)
Menu(staffList)