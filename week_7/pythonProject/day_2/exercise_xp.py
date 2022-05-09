# Exercise 1
import random


def display_message():
    print("I am learning Python at DI Bootcamp!")


display_message()


# Exercise 2: What’s Your Favorite Book ?


def favorite_book(book):
    print(f"One of my favorite book is {book}")


my_book = input("What is your favorite book ? ")
favorite_book(my_book)


# Exercise 3 : Some Geography


def describe_city(city="Paris", country="France"):
    print(f"{city} is in {country}")


city = input("Enter city: ")
country = input("Enter country: ")
if city == '' and country == '':
    describe_city()
else:
    describe_city(city, country)

# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates
# another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display
# a success message, otherwise show a fail message and display both numbers.


def another_random(num):
    rnd_number = random.randint(1, 100)
    if num != rnd_number:
        message = f"Sorry, you entered {num} and the random is {rnd_number}"
    else:
        message = "Great, the numbers are equal"
    return message


print(another_random(47))


# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and
# the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the
# shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size="L", msg="I love Python"):
    print(f"This a shirt in size {size} with the text {msg}")


make_shirt()
make_shirt("M")
make_shirt("S", "Python is easy")

make_shirt(size="S", msg="Made with keywords arguments")

# Exercise 6 : Magicians …
# Instructions
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(),
# which prints the name of each magician in the list.
# Write a function called make_great() that modifies the
# list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the funcyion show_magicians() to see that the list
# has actually been modified.

magicians_list = [
    'Teller',
    'Jerry Sadowitz',
    'Dynamo',
    'Apollo Robbins',
    'Derren Brown',
    'Criss Angel'
]


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


show_magicians(magicians_list)
print("________________")


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The great " + magicians[i]


make_great(magicians_list)
show_magicians(magicians_list)
