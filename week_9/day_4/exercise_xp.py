class Human:
    def __init__(self, name, age, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building.address
        building.add_inhabitant({'name':self.name, 'age': self.age})


class Building:

    def __init__(self, address):
        self.address = address
        self.inhabitants = []

    def add_inhabitant(self, human):
        self.inhabitants.append(human)


class City:

    def __init__(self, name):
        self.name = name
        self.buildings = []

    def construct(self, address):
        self.buildings.append(address.address)


john = Human('John', 24)
alice = Human("Alice", 32)
tom = Human("Tom", 52)
building2 = Building("Bat B")
building1 = Building("Bat A")
john.move(building1)
alice.move(building2)
tom.move(building1)
print(john.living_place)
print(building1.inhabitants)
print(building2.inhabitants)

paris = City("Paris")
paris.construct(building1)
paris.construct(building2)

print(paris.buildings)





