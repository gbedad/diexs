# Exercise 1 Regular expression 1
import re


def extract_numbers(string):
    return "".join(re.findall(r"\d+", string))


print(extract_numbers('k5k3q2g5z6x9bn'))

# Exercise 2 : Regular Expression #2

user_name = input("\nEnter your fullname as Name Lastname: ")


def check_name_validity(name):

    pattern = re.match(r'^[A-Z][a-z]+\s+^[A-Z][a-z]+', name)
    if pattern:
        return True
    else:
        return False


print(check_name_validity(user_name))

# Exercise 3: Python Password Generator
