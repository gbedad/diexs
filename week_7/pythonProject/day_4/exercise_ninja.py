# Exercise 1 : What’s Your Name ?
# Instructions
# Write a function called get_full_name() that takes three arguments:
# 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user,
# the name returned should only contain
# the first and the last name.
from typing import Dict, Any


def get_full_name(first, last, middle=""):
    print(first, middle, last)


get_full_name("Gerald", "Berrebi", "Israel")

# Exercise 2 : From English To Morse
# Instructions
# Write a function that converts English text to morse code and another one
# that does the opposite.
# Hint: Check the internet for a translation table, every letter
# is separated with a space and
# every word is separated with a slash /.

morse_table = dict(a=".-", b="-...", c="-.-.", d="-..", e=".", f="..-.", g="--.", h="....",
                   i="..", j=".---", k="-.-", l=".-..", m="--", n="-.", o="---", p=".--.",
                   q="--.-", r=".-.", s="...", t="-", u="..-", v="...-", w=".--", x="-..-",
                   y="-.--", z="--..")


def alphabet_to_morse(text):
    text = text.lower()
    morse_text = ""
    for char in text:
        if char == ' ':
            morse_table[char] = '/'
        morse_text += f"{morse_table[char]} "
    return morse_text


def morse_to_alphabet(morse):
    text = ""
    morse_as_list = morse.split(" ")
    for code in morse_as_list:
        if code == '/':
            text += " "
        for key, val in morse_table.items():

            if val == code:
                text += key
    print(text)
    return text


print(morse_to_alphabet(".. - / .. ... / -. --- .-- / --- .-. / -. . ...- . .-."))

print(alphabet_to_morse("It is now or never"))
