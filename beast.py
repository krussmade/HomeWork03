from animal import Animal
from enum import Enum


class Diet(Enum):
    PREDATOR = 1
    HERBIVOROUS = 2
    INSECTIVORES = 3



class Beast(Animal):
    def __init__(self, name, weight, diet):
        Animal.__init__(self, name, weight)
        self.name = name
        self.weight = weight
        self.diet = diet


    def Print(self):
        print("Beast: name", self.name, ", weight ", self.weight, ", diet ", self.diet)
        pass


    def FilePrint(self, ostream):
        ostream.write("Beast: name = {}, weight = {}, diet = {}".format(self.name, self.weight, self.diet))
        pass



