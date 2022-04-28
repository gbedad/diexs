import random

# Exercise 1
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list1.extend(list2)
print(list1)

# Exercise 2
"""
    Test Data
    Input the 1st number: 25
    Input the 2nd number: 78
    Input the 3rd number: 87

    The greatest number is: 87
"""
num = int(input("How many numbers ?: "))
list_numbers = []
for i in range(num):
    number = int(input("Enter a number:"))
    list_numbers.append(number)
max_number = max(list_numbers)
print("Max number is : ", max_number)

# Exercise 3 Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the
# letter and whether it's a vowel or a consonant.
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiouy"
for letter in alphabet:
    if letter in vowels:
        print("Vowel", "Message")
    else:
        print("Consonant", "Message")

# Exercise 4 :
# Instructions
# Using this variable
#
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#
# Ask a user for their name, if their name is in the names list print
# out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")
for name in names:
    if name == user_name:
        index = names.index(name)
        print(f"{name} is at index {index}")

# Exercise 5 : Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearance of the
# letter variable in each word of the list.
# If the letter doesn’t exist in one of the words,
# print a friendly message with the word and the letter.

words = []
for count in range(1, 8):
    user_input = input(f"Enter word n{count} :")
    words.append(user_input)
print(words)
letter = input("Enter a letter: ")
for word in words:
    for char in word:
        if letter == char:
            print(f"The letter {letter} is at index {word.index(letter)} in the word {word}")
            break
    if letter not in word:
        print(f"Sorry the letter {letter} is not in {word}")

# Exercise 6 :
# Instructions
# Create a list of numbers from one to one million and
# then use min() and max() to make sure your list actually
# starts at one and ends at one million. Use the sum() function
# to see how quickly Python can add a million numbers.
my_range = range(1, 1000001)
my_list = []
for i in my_range:
    my_list.append(i)
print(min(my_list))
print(max(my_list))
print(sum(my_list))

# Exercise 7 :
# Instructions
# Write a program which accepts a sequence of comma-separated numbers.
# Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
#
# Then, the output should be:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

my_sequence = input("Enter a sequence of comma separated-numbers: ")
my_sequence_list = my_sequence.split(",")
print(my_sequence_list)
my_sequence_tuple = tuple(my_sequence_list)
print(my_sequence_tuple)

# Exercise 8 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better
# luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.



computer_score = 0
user_score = 0
# user_guess = input("Enter a number 1 -9: ")
play = True
while play:
    computer_guess = random.randint(1, 9)
    user_guess = input("Enter a number 1 -9: ")
    if user_guess == str(computer_guess):
        print(user_guess, computer_guess)
        print("Winner")
        user_score += 1
        print(f"Computer score: {computer_score}, user score : {user_score}")
    elif int(user_guess != str(computer_guess)) and user_guess != 'quit':
        print(user_guess, computer_guess)
        print("Better luck next time")
        computer_score += 1
        print(f"Computer score: {computer_score}, user score : {user_score}")
    elif user_guess == 'quit':
        print(user_guess, computer_guess)
        print(f"Computer score: {computer_score}, user score : {user_score}")
        play = False




