import io
import time


sowpods = io.open("sowpods.txt", encoding="utf8").read().split("\n")

class CustomRandom():
    seedVal:int
    
    def __init__(self, seed = 3):
        self.seedVal = seed
    
    def seed(self, seed:int):
        self.seedVal = seed
    
    def random(self) -> int:
        self.seedVal = time.time_ns()
        return round((self.seedVal * time.time()) % len(sowpods))

rdm = CustomRandom()

num = rdm.random()
print(sowpods[num])