# angle = float(input())
angle = 150.0

def convertToRadian(angle) -> float:
    return angle*3.14/180

print("Degrees:", angle)
print("Radians:", convertToRadian(angle))