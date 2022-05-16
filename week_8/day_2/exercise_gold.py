# Exercise 1 Geometry

import random


class Circle:
    def __init__(self, radius=1.0):
        self.area = (3.14*radius**2)/4
        self.perimeter = 2*3.14*radius

    def definition(self):
        print(f"The circle surface is {self.area} cm2 and its perimeter is {self.perimeter} cm")


circle1 = Circle()
circle1.definition()

# Exercise 2 Custom list class


class MyList:
    def __init__(self, list_item):
        self.list_item = list_item

    def reverse_list(self):
        print(self.list_item[::-1])

    def sort_list(self):
        print(sorted(self.list_item, reverse=True))
        return sorted(self.list_item, reverse=True)

    def create_new_list(self):
        random_list = []
        length = len(self.list_item)
        for i in range(length):
            num = random.randint(0, 100)
            random_list.append(num)
        print(random_list)



new_list = MyList([45, 2, 6, 0, 3])

new_list.reverse_list()
new_list.sort_list()

new_list.create_new_list()

# Exercise 3: Restaurant Menu Manager
# see file menu_manager.py.
