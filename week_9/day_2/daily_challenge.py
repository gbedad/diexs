# Circle
import math


class Circle:
    circles = []

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    @classmethod
    def from_diameter(cls, name, diameter):
        return cls(name=name, radius=diameter/2)

    def compute_area(self):
        return math.pi*self.radius**2

    def print_circle(self):
        print(f"Circle {self.name} of radius {self.radius} and area {self.compute_area()}")

    def compare_circles(self, b):
        if self.compute_area() > b.compute_area():
            return f'The circle {self.name} is bigger than {b.name}'
        elif self.compute_area() < b.compute_area():
            return f'The circle {b.name} is bigger than {self.name}'
        else:
            return f"The circles are equal"

    @classmethod
    def add_circles(cls, c):
        cls.circles.append(c.name)


my_circle1 = Circle(name='A', radius=30)
my_circle2 = Circle.from_diameter(name='B', diameter=60)
print(my_circle1.compute_area())
Circle.add_circles(my_circle1)
Circle.add_circles(my_circle2)


print(my_circle1.compare_circles(my_circle2))
print(Circle.circles)
# my_circle2 = Circle(diameter=60)
# my_circle2 = Circle.from_diameter(45)

# print(my_circle1.radius)
# print(my_circle2.diameter)
# print(my_circle2.radius)
