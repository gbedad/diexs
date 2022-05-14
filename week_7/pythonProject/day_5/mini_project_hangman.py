# Mini project hangman
import random

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


def check_if_win(guessed, secret_word):
    if len(guessed) == len(secret_word):
        return True
    else:
        return False


wrong_letters = ''
correct_letters = ''
guessed_letters = wrong_letters + correct_letters


while True:
    display_game(wrong_letters, correct_letters, secret_word=word)
    letter = input_letter(already_guessed=correct_letters + wrong_letters)
    print(guessed_letters)
    if letter in word:
        correct_letters += letter
        check = check_if_win(correct_letters, word)
        if check:
            display_game(wrong_letters, correct_letters, secret_word=word)
            print("You have guessed the word.")
            break
    else:
        wrong_letters += letter
        if len(wrong_letters) == len(HANGMAN) - 1:
            display_game(wrong_letters, correct_letters, secret_word=word)
            print(f"No more trials, the word was: '{word}'.")
            break










