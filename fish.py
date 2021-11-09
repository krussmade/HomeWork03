from animal import Animal
from enum import Enum

class Habitat(Enum):
    SEA = 1
    LAKE = 2
    RIVER = 3
    OCEAN = 4
    POND = 5

class Fish(Animal):
    def __init__(self, name, weight, habitat):
        Animal.__init__(self, name, weight)
        self.name = name
        self.weight = weight
        self.habitat = habitat


    def Print(self):
        print("Fish: name", self.name, ", weight ", self.weight, ", habitat ", self.habitat)
        pass


    def FilePrint(self, ostream):
        ostream.write("Fish: name = {}, weight = {}, habitat = {}".format(self.name, self.weight, self.habitat))
        pass
