class Fridge():
    
    #Fields
    items = {}
    
#     Constructor
    def __init__(self):
        return
    
    #Methods
    def store(self, item):
        if (item in self.items):
            self.items[item] += 1
        else:
            self.items[item] = 0
        print(item, "has been stored.")
        return
    
    def retrieve(self, item):
        if (item in self.items):
            if (self.items[item] > 0):
                self.items[item] -= 1
                print(item, "was retrieved from the fridge")
            else:
                print("You don't have", item, "in stock anymore!")
        else:
            print(item, "does not exist in the fridge")
        return
    
    def view(self):
        return