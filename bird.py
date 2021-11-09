from animal import Animal

class Bird(Animal):
    def __init__(self, name, weight, isMigration):
        Animal.__init__(self, name, weight)
        self.name = name
        self.weight = weight
        self.isMigration = isMigration


    def Print(self):
        print("Bird: name", self.name, ", weight ", self.weight, ", isMigration ", self.isMigration)
        pass


    def FilePrint(self, ostream):
        ostream.write("Bird: name = {}, weight = {}, isMigration = {}".format(self.name, self.weight, self.isMigration))
        pass
