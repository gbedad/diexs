# Exercise 1
print("Hello world\n"*4)

# Exercise 2
number = (99**3)*8
print(f"The result of (99^3)*8 is {number}")

# Exercise 3
# 5 < 3 False
# 3 == 3 True
# 3 == "3" False
# "3" > 3 False
# "Hello" == "hello" False

# Exercise 4
computer_brand = input("Enter your computer brand : ")
if computer_brand[0] in "aeiou":
    print(f"I have an {computer_brand} computer.")
else:
    print(f"I have a {computer_brand} computer.")


# Exercise 5
"""
Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it’s value to an interesting sentence
about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
Have your code print the info message.
Run your code
"""
name = "Gerald"
age = 12
shoe_size = 39
info = f"My name is {name} and I am {age} years old." \
       f"I am sad because the shoes that I want start a size 40 " \
       f"and mine is {shoe_size}. "
print(info)

# Exercise 6
"""
Create two variables, a and b.
Each variables value should be a number.
If a is bigger then b, have your code print Hello World.
"""
a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
if a > b:
    print("Hello world")
else:
    print("b is bigger than a")

# Exercise 7 Odd or Even
num = int(input("Enter an integer number: "))
if num == 0:
    print("O is neither odd or even")
elif num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Exercise 8 What's your  name
"""
Write code that asks the user for their name and determines whether or not you have the same name,
print out a funny message based on the outcome.
"""
my_name = "Gerald"
input_name = input("Enter your name: ")
if my_name == input_name:
    print("So nice, we have the same name!")
else:
    print(f"Never-mind, {input_name}, your name is not that bad! ")

# Exercise 9: Tall Enough To Ride A Roller Coaster
"""
Write code that will ask the user for their height in inches.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride.
"""
print("Your height should be more than 145 inches to ride a roller coaster")
input_height = int(input("Enter your height in inches: "))
if input_height > 145:
    print(f"Your height is {input_height} inches, you are tall enough to ride.")
else:
    print(f"Sorry, your height is only {input_height} inches, you need to grow some more to ride.")
