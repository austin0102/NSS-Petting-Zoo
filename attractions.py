class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithering serpents of all shapes and sizes"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "water-loving creatures in their natural habitat"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)
