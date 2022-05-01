# Exercise 1: List Of Integers - Randoms
# Instructions
# Continuation of the Exercise 2 XP NINJA - from Week4Day2
# Instead of asking the user for 10 integers, generate 10 random
# integers yourself. Make sure that these random integers are between -100 and 100.
# Instead of always generating 10 integers, let the amount of integers
# also be random! Generate a random positive integer no smaller than 50.
# Will the code work when the number of random numbers is not equal to 10?
import random

random_list = []
for i in range(10):
    random_list.append(random.randint(-100, 101))
print(random_list)

for i in range(random.randint(50, 100)):
    random_list.append(random.randint(-100, 101))
print(random_list)

# Exercise 2: Authentication CLI - Login:
# Instructions
# Create a dictionary that contains users: each key will represent
# a username, and each value will represent that user’s password.
# Initialize this dictionary with 3 users & passwords.
# Create a loop that does the following:
# If the user inputs “exit”, break out of the loop.
# If the user inputs “login”, ask them for their username and password.
# If the user’s details exist print “you are now logged in”.
# If the user is successfully logged in, store the username
# in a variable called logged_in so we can track it later.

users ={
        "user1": "1234",
        "user2": "4567",
        "user3": "9999",
    }

print("Choices : exit, login")
user_input = input("Enter your choice: ")

if user_input == 'exit':
    print("Bye")
elif user_input == 'login':
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # for (username, password) in users.items():
    flag = True
    while flag:
        if (username, password) in users.items():
            print("You are logged in!")
            logged_in = username
            print(f"User logged in : {logged_in}")
            # break
            flag = False
        elif username not in users.keys():
            user_answer = input("User doesn't exit, do you want to signup?(y/n) ")
            if user_answer == "y":
                new_username = username
                new_password = input("Enter a password: ")
                users.update({new_username: new_password})
                flag = False
            else:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
        elif password not in users.values():
            print("Invalid password!")
            password = input("Enter your password: ")
print(users)

# Exercise 3: Authentication CLI - Signup:
# Instructions
# Continuation of the Exercise Above - Authentication CLI - login
#
# If the user does not exist ask if they would like to sign up:
# Ask the user for a username and make sure it doesn’t exist
# as a key in our dictionary, if the username is not valid
# continue asking the user to input a username.
# Ask the user for a password. The password is the value.

