yourNum:int = int(input("Enter a number from 0 to 100: "))

guesses:int = 1

def binarySearch(low:int, high:int, num:int):
    global guesses
    if low == high:
        print("Number not found")
        return
    else:
        mid:int = (low+high)//2
        if mid == num:
            print("Number found!!!")
            return
        elif num > mid:
            print("Too Low!")
            guesses += 1
            binarySearch(mid, high, num)
        elif num < mid:
            print("Too High!")
            guesses += 1
            binarySearch(low, mid, num)

binarySearch(0, 100, yourNum)
print()
print("Number of guesses:", guesses)