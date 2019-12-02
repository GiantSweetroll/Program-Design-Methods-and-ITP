def is_member(x, a:list)->bool:
    i = 0
    while(i<len(a)):
        if(x == a[i]):
            return True
        i+=1
    
    return False

print(is_member(12, [1, 3, 12, 34]))