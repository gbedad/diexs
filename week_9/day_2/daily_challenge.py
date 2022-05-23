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

    def __str__(self):
        return f"Circle {self.name} of radius {self.radius} and area {round(self.compute_area(), 1)}"

    # def compare_circles(self, b):
    #     if self.compute_area() > b.compute_area():
    #         return f'The circle {self.name} is bigger than {b.name}'
    #     elif self.compute_area() < b.compute_area():
    #         return f'The circle {b.name} is bigger than {self.name}'
    #     else:
    #         return f"The circles are equal"

    def __add__(self, other):
        return f" New circle of radius: {self.radius + other.radius}"

    def __gt__(self, other):
        if self.radius > other.radius:
            print(f"{self.name} is bigger than {other.name}")
            return True
        elif self.radius < other.radius:
            print(f"{self.name} is smaller than {other.name}")
            return
        else:
            return f"{self.name} and {other.name} are equal"

    @classmethod
    def add_circles_to_list(cls, a, b):
        cls.circles.append(a.name)
        cls.circles.append(b.name)
        print(cls.circles)
        if a > b:
            cls.circles[0] = b.name
            cls.circles[1] = a.name
        else:
            cls.circles[0] = a.name
            cls.circles[1] = b.name
        return cls.circles


my_circle1 = Circle(name='A', radius=30)
my_circle2 = Circle.from_diameter(name='B', diameter=30)

print("add circles", my_circle1 + my_circle2)
print(str(my_circle2))

print(my_circle1 > my_circle2)
print(my_circle1.compute_area())
print(Circle.add_circles_to_list(my_circle1, my_circle2))


# print(my_circle1.compare_circles(my_circle2))
# print(Circle.circles)
# my_circle2 = Circle(diameter=60)
# my_circle2 = Circle.from_diameter(45)

# print(my_circle1.radius)
# print(my_circle2.diameter)
# print(my_circle2.radius)
