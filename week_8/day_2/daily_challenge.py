class Farm:
    def __init__(self, name):
        print(f"{name}'s farm")
        self.name = name
        self.animal_dict = {}

    def add_animal(self, animal, number=1):
        if animal in self.animal_dict.keys():
            self.animal_dict[animal] += 1
        else:
            self.animal_dict[animal] = number

    def get_info(self):
        for k, v in self.animal_dict.items():
            print(f"{k}: {v}")

    def get_animal_types(self):
        list_animals = []
        for key in self.animal_dict.keys():
            list_animals.append(key)
        print(sorted(list_animals))
        return sorted(list_animals)

    def get_short_info(self):
        the_animals = self.get_animal_types()
        the_animals_string = ",".join(the_animals[0:len(the_animals)-1])+" and "+the_animals[len(the_animals)-1]
        print(f"{self.name} farm has {the_animals_string}.")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
macdonald.get_short_info()