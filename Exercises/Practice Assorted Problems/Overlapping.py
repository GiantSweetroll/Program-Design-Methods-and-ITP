def overlapping(lst1, lst2)->bool:
    for item1 in lst1:
        for item2 in lst2:
            if (item1 == item2):
                return True
    
    return False

print(overlapping([1, 5, 3], [1, 2, 66]))
print(overlapping([4, 5, 6], [1, 2, 3]))  