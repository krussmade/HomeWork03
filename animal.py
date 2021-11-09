
class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


    def Print(self):
        pass


    def FilePrint(self, ostream):
        pass


    def SomeParameter(self):
        sum: int = 0
        for item in self.name:
            sum += ord(item)
        return sum / self.weight

