from TA_Projects.Fridge.container.container import Container
from TA_Projects.Fridge.item.item import Item

class FridgePart():
    
    #Fields
    containers:[Container]
    __name:str
    
    #Constructor
    def __init__(self, name:str):
        self.containers = []
        self.__name = name
        
    #Methods
    def getMaxCapacity(self) -> int:
        total = 0
        for container in self.containers:
            total += container.getMaxSpace()
        return total
    
    def getRemainingCapacity(self) -> int:
        total = 0
        for container in self.containers:
            total += container.getRemainingCapacity()
        return total
    
    def addContainer(self, container:Container):
        self.containers.append(container)
        
    def getName(self) -> str:
        return self.__name
    
    def put(self, item:Item, amount:int, containerIndex:int):
        container:Container = self.containers[containerIndex]
        if container.getPrefferedItem() != Container.ANY:
            if item.getItemType() == container.getPrefferedItem():
                self.__put(item, amount, container)
            else:
                prefItem:str = container.getPrefferedItem
                while(True):
                    response:str = input("What you are putting there isn't a ", prefItem + ",", "are you sure? (Y/N):")
                    response.casefold()
                    if response == "y".casefold():
                        self.__put(item, amount, container)
                    elif response == "n".casefold():
                        print(amount, item.getName(), "was not stored.")
                        #TO-DO option to change storage
                        break
                    else:
                        print("Invalid input, please try again.")
        else:
            self.__put(item, amount, container)
            
    def take(self, item:Item, amount:int, containerIndex:int):
        container:Container = self.containers[containerIndex]
        if amount < 0:
            removed:bool = container.removeAllItem(item)
            if removed:
                print("All", item.getName(), "was removed from the", self.getName() + "'s", container.getName())
            else:
                print(item.getName(), "was not found in the", self.getName() + "'s", container.getName())
        else:
            removed:bool = container.removeItem(item, amount)
            if removed:
                print(amount, item.getName(), "was removed from the", self.getName() + "'s", container.getName() + ",", "with", container.getItemRemaining(item), "remaining")
            else:
                print(item.getName(), "was not found in the", self.getName() + "'s", container.getName())
                
    def getItemRemaining(self, item:Item, containerIndex:int) -> int:
        return self.containers[containerIndex].getItemRemaining(item)
    
    #Private Methods
    def __put(self, item:Item, amount:int, container:Container):
        if (container.getSpaceLeft() > amount):
            container.store(item, amount)
            print(amount, item.getName(), "stored.")
        else:
            print("Storage is full!")
            #TO-DO add operation for when storage is full