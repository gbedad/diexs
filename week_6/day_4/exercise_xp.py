
# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
import math

my_fav_numbers = {3, 7, 11, 15, 30, 8, 26}
my_fav_numbers.add(13)
my_fav_numbers.add(17)
print(my_fav_numbers)
my_fav_numbers.remove(26)
print(my_fav_numbers)
friend_fav_numbers = {12, 37, 34, 67}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
for number in range(1, 21):
    print(number)

# Exercise 4
i = 1
while i <= 5:
    i1 = math.modf(i)
    if i1[0] == 0:
        i = int(i)
        print(i)
    else:
        print(i)
    i += 0.5

# Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Basket initial", basket)
basket.remove("Banana")
print("Basket after removing banana", basket)
basket.remove("Blueberries")
print("Basket after removing blueberries", basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print("Basket after adding apples", basket)
apples = []
for fruit in basket:
    if fruit == 'Apples':
        apples.append(fruit)
number_of_apples = len(apples)
print("Number of apples", number_of_apples)
print(basket)

for fruit in range(len(basket)):
    basket.pop()
print("Empty basket", basket)

# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user
# for their name, unless the input is equal to your name.
my_name = "gerald"
user_name = ""
while user_name != my_name:
    user_name = input("Enter your name: ")
    user_name = user_name.lower()
print("Good choice")

# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.

my_list = ["Banana", "Apples", "Oranges", "Blueberries", "Kiwi", "Mango", "Strawberries"]

for index in range(1, len(my_list)):
    if index % 2 != 0:
        continue
    print(my_list[index])

# Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500
# and prints all multiples of 5 and 7.

for i in range(1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
    else:
        continue

# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits
# with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words
# into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list,
# print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print,
# “You chose a new fruit. I hope you enjoy”.
user_fav_fruits = input("Enter your favorite fruits separated by space: ")
user_fav_fruits_list = user_fav_fruits.split(" ")
user_input = input("Enter a fruit : ")
is_present = False
for fruit in user_fav_fruits_list:
    if user_input == fruit:
        is_present = True
if not is_present:
    user_fav_fruits_list.append(user_input)
message = "You chose one of your favorite fruits! Enjoy!" if is_present else "You chose a new fruit. I hope you enjoy"
print(message)
print("Your favorite fruits", user_fav_fruits_list)

# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings,
# when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying
# you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the
# pizza pie and what the total price is (10 + 2.5 for each topping).

flag = True
pizza_price = 10
topping_price = 2.5
topping_list = []
number_of_toppings = len(topping_list)
while flag:
    topping = input("Enter a topping:('quit' to end) ")
    print(f"you’ll add {topping} to your pizza")
    topping_list.append(topping)
    if topping == "quit":
        topping_list.remove("quit")
        flag = False
toppings = ",".join(topping_list)
number_of_toppings = len(topping_list)

print(f"You have ordered a pizza with these toppings: {toppings}.")
print(f"The total cost will be ${pizza_price + number_of_toppings*topping_price }")

# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie
# that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints
# a list of the teens who are permitted to watch the movie.

total_price = 0
is_family = True
while is_family:
    person_age = int(input("What is your age (type '0' to issue the ticket: "))
    if 0 > person_age < 3:
        ticket = 0
        total_price += ticket
    elif 3 <= person_age <= 12:
        ticket = 10
        total_price += ticket
    elif person_age > 12:
        ticket = 15
        total_price += ticket
    elif person_age == 0:
        is_family = False
        print(f"The total cost for the family is ${total_price}")

teenagers_list = ["John", "Bob", "Charlie", "Anna", "Rachel"]
teens_permitted = []
for teen in teenagers_list:
    ask_age = int(input(f"{teen} what is your age ?: "))
    if 16 <= ask_age <= 21:
        teens_permitted.append(teen)

print("Teens permitted", teens_permitted)


# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user
# for their age, if they are less than 16 years old remove them from the list.
# At the end, print the final list.

names = ["john", "bob", "anna", "rachel", "tom"]
final_list = []
for name in names:
    age = int(input(f"{name}, how old are you ?: "))
    if age > 16:
        final_list.append(name)

print("Final list", final_list)

#  Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of
# various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich
# that was made , such as I made your tuna sandwich.

sandwich_orders = ["tuna", "salmon", "pastrami"]
finished_sandwiches = []
is_complete = False
is_ready = ""
while len(sandwich_orders) > 0 and is_ready != "end":
    is_ready = input("Enter the sandwich when finished :(end when finished inputs): ")
    for sandwich in sandwich_orders:
        if is_ready == sandwich:
            sandwich_orders.remove(is_ready)
            finished_sandwiches.append(is_ready)
        if len(sandwich_orders) == 0:
            is_complete = True

for finished in finished_sandwiches:
    print(f"Your {finished} is ready")
if is_complete:
    print("All sandwiches are ready")

# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure
# the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message
# saying the deli has run out of pastrami, and then use a while loop
# to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders = ["tuna", "salmon", "pastrami", "veggie", "pastrami", "cheese", "pastrami"]
print("List of ordered sandwiches", sandwich_orders)
print(">>> The deli has run out of pastrami...")
print(">>> We have to cancel all pastrami sandwiches!")
for sandwich in sandwich_orders:
    if sandwich == "pastrami":
        sandwich_orders.remove(sandwich)
print("The sandwich order list is now: ", sandwich_orders)
