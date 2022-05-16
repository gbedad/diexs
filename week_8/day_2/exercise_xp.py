# Exercise 1 Cats

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

felix = Cat("Felix", 5)
blacky = Cat("Blacky", 4)

def find_oldest(inst1, inst2):
    if inst1.age > inst2.age:
        return inst1.name, inst1.age
    else:
        return inst2.name, inst2.age

oldest = find_oldest(felix, blacky)
print(oldest)
print(f"The oldest cat is {oldest[0]}, and is {oldest[1]} years old.”")

# print(find_oldest(felix, blacky))

# Exercise 2 Dogs


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm!")


davids_dog = Dog("Rex", 50)
print(f"David's dog name is {davids_dog.name} and it measures {davids_dog.height} cm.")
davids_dog.jump()
davids_dog.bark()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog name is {sarahs_dog.name} and it measures {sarahs_dog.height} cm.")
sarahs_dog.jump()
sarahs_dog.bark()

if sarahs_dog.height > davids_dog.height:
    print(f"The biggest dog is {sarahs_dog.name}")
else:
    print(f"The biggest dog is {davids_dog.name}")

# Exercise 3: who is the song producer


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_song(self):
        for item in self.lyrics:
            print(item)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_song()

# Exercise 4 : Afternoon At The Zoo


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print("Animal already exists")

    def get_animals(self):
        print(f"{self.name} animals")
        print("-"*(len(self.name) + 8))
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold")
        else:
            print(f"{animal_sold} is not in {self.name}")

    def sort_animals(self):
        self.animals.sort()
        first_letters = []
        for animal in self.animals:
            first_letters.append(animal[0])
        groups = {}
        for letter in first_letters:
            groups[letter] = list(filter(lambda s: s[0] == letter, self.animals))
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        print("\nGroups of animals in alphabetical order")
        print(groups)




ramat_gan_safari = Zoo("Ramat Gan Safari")

def manage_animals():
    buy_animal = input("Which animal do you want to add? ")
    ramat_gan_safari.add_animal(buy_animal)

add_new = True
while add_new:
    manage_animals()
    again = input("Another animal? (y/n) ")
    if again == 'n':
        add_new = False

# print(ramat_gan_safari.animals)
# zebra = ramat_gan_safari.add_animal("zebra")
# print(ramat_gan_safari.animals)
#
# ramat_gan_safari.get_animals()
#
# ramat_gan_safari.sell_animal("zebra")
# ramat_gan_safari.get_animals()
#
# giraffe = ramat_gan_safari.add_animal("Lion")
# zebra = ramat_gan_safari.add_animal("Tiger")
# giraffe = ramat_gan_safari.add_animal("Ape")
# zebra = ramat_gan_safari.add_animal("Baboon")
# giraffe = ramat_gan_safari.add_animal("Bear")
# zebra = ramat_gan_safari.add_animal("Cougar")
# zebra = ramat_gan_safari.add_animal("Cat")
# giraffe = ramat_gan_safari.add_animal("Eel")
# zebra = ramat_gan_safari.add_animal("Emu")

ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()

ramat_gan_safari.get_groups()