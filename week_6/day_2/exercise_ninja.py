# Exercise 1 PATH
# My Python PATH is : "/Users/geraldberrebi/PycharmProjects/pythonProject2/venv/bin/python"

# Exercise 2
# I have created a temporary alias of python with alias="python3". When I run py, I open the python console.

# Exercise 3
"""
    >>> 3 <= 3 < 9 True
    >>> 3 == 3 == 3 True
    >>> bool(0) False
    >>> bool(5 == "5") False
    >>> bool(4 == 4) == bool("4" == "4") True
    >>> bool(bool(None)) False
"""
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x) # True
print("y is", y) # False
print("a:", a) # 1 + 4 = 5
print("b:", b) # 0 + 10 = 10

# Exercise 4 : How Many Characters In A Sentence ?
"""
Instructions
Use python to find out how many characters are in the following text,
use a single line of code (beyond the establishment of your my_text variable).
"""
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(f"This text have {len(my_text)} characters.")

# Exercise 5: Longest Word Without A Specific Character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

sentence = input("Enter the longest word without A: ")
last_sentence: str = sentence
while "a" in sentence:
    sentence = input("Error, this sentence contain a. Enter the longest word without A: ")
sentence = input("Enter a longer word without A: ")
while len(sentence) > len(last_sentence):
    last_sentence = sentence
    print("Congratulations, Your sentence is longer")
    sentence = input("Enter again: ")
    if len(sentence) < len(last_sentence) or "a" in sentence:
        print("Bye")



