def calc_weight_on_planet(weightOnEarth, surfaceGravity =  23.1)->float:
    # weight is equal to mass times surface gravity
    mass = weightOnEarth/9.8
    return mass*surfaceGravity

print(calc_weight_on_planet(120, 9.8))
print(calc_weight_on_planet(120))
print(calc_weight_on_planet(120, 23.1))