# Exercise 1 Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamois(Cat):
    def sing(self, sounds):
        return f'{sounds}'


roy = Chartreux("Roy", 3)
bob = Siamois("Bob",4)
felix = Bengal("Tiger", 3)
my_cats = [roy, felix, bob]

my_pets = Pets(my_cats)

my_pets.walk()

# Exercise 2 Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        running_speed = self.weight/self.age*10
        return running_speed

    def fight(self, other_dog):
        dog1 = self.run_speed()*self.weight
        print(dog1)
        dog2 = other_dog.run_speed()*other_dog.weight
        print(dog2)
        winner = self.name if dog1 > dog2 else other_dog.name
        return f"{winner} is the winner"


rex = Dog("Rex", 3, 34)
bob = Dog("Bob", 4, 28)
tom = Dog("Tom", 2, 45)

print(tom.fight(rex))

# Exercise 3 Dogs domesticated

# See file dogs_domesticated which is importing Dog class
