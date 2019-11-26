#Suppose you are writing a blog and you have an image that is m units wide and n units high but your blog
#only has space for an image that is z units wide (where z is less than m)

def calc_new_height()->float:
    width = int(input("Enter the current width: "))
    height = int(input("Enter the current height: "))
    widthDesired = int(input("Enter the desired width: "))
    
    widthToHeightRatio = height/width
    heightDesired = widthDesired * widthToHeightRatio
    
    print("The corresponding height is:", heightDesired)
    return heightDesired
    
    
print(calc_new_height())