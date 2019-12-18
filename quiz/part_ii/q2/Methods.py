def sortStaffByName(staff:[]):
    for i in range(len(staff)-1):
        for a in range(i+1, len(staff)):
            if staff[i].name > staff[a].name:
                temp = staff[i]
                staff[i] = staff[a]
                staff[a] = temp