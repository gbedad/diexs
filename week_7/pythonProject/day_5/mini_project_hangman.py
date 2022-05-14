# Mini project hangman
import random
import re

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']

HANGMAN = [
    """
    +---+
        |
        |
        |
       === 
    """,
    """
    +---+
    O   |
        |
        |
       === 
    """,
    """
    +---+
    O   |
    |   |
        |
       === 
    """,
    """
    +---+
    O   |
   /|   |
        |
       === 
    """,
    """
    +---+
    O   |
   /|\  |
        |
       === 
    """,
    """
    +---+
     O  |
    /|\ |
    /   |
       === 
    """,
    """
    +---+
     O  |
    /|\ |
    / \ |
       === 
    """
]

word = random.choice(wordslist)


# def check_letter(letter, secret_word):
#     for i in range(len(word)):
#         if letter == word[i]:
#             secret_word = secret_word[0:i]+letter+secret_word[i+1:]
#     return secret_word
#
#
# def show_secret(secret_word, correct_letters, wrong_letters, letter):
#     s_secret = "*"*len(secret_word)
#     print(HANGMAN[len(wrong_letters)])
#     s_secret = check_letter(letter, secret_word)
#     return s_secret
#
#
# def input_letter():
#     user_input = input("Enter a letter: ")
#     if user_input in guessed_letters:
#         print("This letter was already chosen, try again")
#     return user_input
#
#
# def play():
#     while True:
#         secret = show_secret(secret_word=word, correct_letters=correct_letters, wrong_letters=wrong_letters)
#         letter = input_letter()
#         show_secret(secret_word=secret, wrong_letters=wrong_letters, correct_letters=correct_letters)
#         check_letter(letter=letter, secret_word=word)
#
#
# correct_letters = []
# wrong_letters = []
# guessed_letters = correct_letters+wrong_letters
#
#
# play()
#
# print(guessed_letters)

def display_game(wrong_letters, correct_letters, secret_word):
    secret = "*"*len(word)
    print(HANGMAN[len(wrong_letters)])
    print(f"Wrong letters: {wrong_letters}")
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            secret = secret[0:i] + secret_word[i] + secret[i+1:]
    print(secret)


def input_letter(already_guessed):
    while True:
        user_input = input("Choose a letter: ")
        user_input = user_input.lower()
        if user_input == ':':
            break
        elif len(user_input) != 1:
            print("Only one letter")
        elif user_input in already_guessed:
            print("This letter was already chosen.")
        else:
            return user_input


def check_if_win(secret):
    if secret == word:
        print("You have guessed the correct word.")





wrong_letters = ''
correct_letters = ''
guessed_letters = wrong_letters + correct_letters

while True:
    display_game(wrong_letters, correct_letters, secret_word=word)
    letter = input_letter(already_guessed=guessed_letters)
    if letter in word:
        correct_letters += letter
    else:
        wrong_letters += letter
        if len(wrong_letters) == len(HANGMAN) - 1:
            display_game(wrong_letters, correct_letters, secret_word=word)
            print(f"No more trials, the word was: '{word}'.")
            break










