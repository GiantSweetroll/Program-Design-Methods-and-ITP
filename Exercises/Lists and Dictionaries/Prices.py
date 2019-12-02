prices = {"banana": 4,
            "apple": 2,
            "orange": 1.5,
            "pear": 3}

for key in prices:
    print(key)
    print("price:", prices[key])
    print("stock:", 0)
    print()
    
total = 0

for key in prices:
    print(0 * prices[key])
    total += 0 * prices[key]
    
print(total)