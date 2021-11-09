from beast import Beast
from bird import Bird
from fish import Fish
from beast import Diet
from fish import Habitat
import string
import random

class Container:
    # Конструктор, инициализируем список фигур
    def __init__(self):
        self.store = []


    # Вывод содержимого в консоль
    def Print(self):
        print("Container is store", len(self.store), "animals:")
        for animal in self.store:
            animal.Print()
        pass

    # Вывод содержимого в файл
    def Write(self, ostream):
        for animal in self.store:
            animal.Write(ostream)
        pass

    def FileFill(self, ifile):
        animalCount = 0
        while True:
            line = ifile.readline()

            if not line:
                break

            info = line.split()
            animalType = info[0]
            if animalType == 'beast':
                animal = Beast(info[1], int(info[2]), Diet(int(info[3])))
            elif animalType == 'bird':
                animal = Bird(info[1], int(info[2]), bool(int(info[3])))
            elif animalType == 'fish':
                animal = Fish(info[1], int(info[2]), Habitat(int(info[3])))
            else:
                continue
            animalCount += 1
            self.store.append(animal)
        return animalCount

    def RandomFill(self, amount):
        for i in range(amount):
            k = random.randint(1, 4)
            if k == 1:
                name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 21)))
                animal = Beast(name, random.randint(100, 1000) + random.random(), Diet(random.randint(1, 3)))
            elif k == 2:
                name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 21)))
                animal = Bird(name, random.randint(100, 500), bool(random.randint(200, 1000)))
            else:
                name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 21)))
                animal = Fish(name, random.randint(100, 500) + random.random(), Habitat(random.randint(1, 5)))
            self.store.append(animal)

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.store[i] < self.store[l]:
            largest = l

        if r < n and self.store[largest] < self.store[r]:
            largest = r

        if largest != i:
            self.store[i], self.store[largest] = self.store[largest], self.store[i]
            self.heapify(n, largest)


    def heapSort(self):
        n = len(self.store)
        for i in range(n, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.store[i], self.store[0] = self.store[0], self.store[i]
            self.heapify(i, 0)



