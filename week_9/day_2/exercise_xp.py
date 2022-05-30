# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them
# take a look at the python documentation online.
# Write a program which prints the results of the following python
# built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation
# which explains the execution of your code. Take a look at the
# doc method on google for help.

def fake_abs(num): # you can do it in just single line by: return (-1) * num if num < 0 else num
    if num < 0:
        return (-1) * num
    return num


print(fake_abs(3))


def fake_int(num):
    if isinstance(num, float):
        return round(num)
    elif isinstance(num, str):
        num_to_number = num * 1 # return in one line like: return num * 1 also rather then multiple by 1 just do casting
        return num_to_number
    return num


print(fake_int('3'))


# Exercise 2


class Currency:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __int__(self):
        return int(self.value)

    def __str__(self):
        if self.value == 1:
            return f"{self.value} {self.name}"
        return f"{self.value} {self.name}s" # you can do in a single line, remeber inside the {} we can run python code, think how to do it :)

    def __repr__(self):
        if self.value == 1:
            return f"{self.value} {self.name}"
        return f"{self.value} {self.name}s"

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.name != other.name:
                raise TypeError(f"Cannot add between Currency type {self.name} and {other.name}")
            return self.value + other.value if self.name == other.name else f"Cannot add between Currency type {self.name} and {other.name}"
        return f"{self.value + other} {self.name}s"

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.name != other.name:
                raise TypeError(f"Cannot add between Currency type {self.name} and {other.name}")
            return f"{self.value + other.value} {self.name}s" if self.name == other.name else f"Cannot add between Currency type {self.name} and {other.name}"
        return f"{self.value + other} {self.name}s"


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1)
print(str(c4))

print(int(c1))

print(c1 + c2)
print(c1 + 11.89)

c3 += c4
print(str(c1))

c4 += 37
print(str(c4))

print(c1)

help(print)
