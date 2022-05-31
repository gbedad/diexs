# Exercise 1 Regular expression 1
import random
import re


def extract_numbers(string):
    return "".join(re.findall(r"\d+", string))


print(extract_numbers('k5k3q2g5z6x9bn'))

# Exercise 2 : Regular Expression #2

user_name = input("\nEnter your fullname as Name Lastname: ")


def check_name_validity(name):
    reg = r"^[A-Z][a-z]+\s[A-Z][a-z]+$"
    pattern = re.compile(reg)
    pattern = re.match(pattern, name)
    if pattern:
        return True
    else:
        return False


print(check_name_validity(user_name))

# Exercise 3: Python Password Generator


def test_password(password):
    reg = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-~'`=]).{6,30}$"
    pattern = re.compile(reg)
    valid_password = re.search(pattern, password)
    if valid_password:
        return "The password is valid"
    else:
        return "Invalid password"


def set_password_length():
    v_length = False
    while not v_length:
        user_input = input("Enter password length (6-30): ")
        if not re.match(r'\d+', user_input):
            v_length = False
        elif 6 <= int(user_input) <= 30:
            v_length = True

    return user_input


def main(a):
    # length = int(set_password_length())
    generated_password = ''
    for i in range(a):
        c = chr(random.randint(33, 123))
        if 91 <= i <= 95:
            continue
        generated_password += c
    return generated_password


# test = main()
# print(test)

# print(test_password(password=test))/
#
# for i in range(100):
#     for j in range(6, 31):
#         test = main(j)
#         print(test)
#         print(test_password(test))


