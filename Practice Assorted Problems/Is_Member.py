def is_member(x, a:list)->bool:
    for i in range(len(a)):
        if(x == a[i]):
            return True
    
    return False

print(is_member(12, [1, 3, 12, 34]))