import random

# Create a string
my_string = input("Enter a string with 10 characters: ")

my_string_length = len(my_string)

if my_string_length < 10:
    print(f"string not long enough, only {my_string_length} long")
elif my_string_length > 10:
    print(f"string too long, {my_string_length} characters")
print(f"The first letter is {my_string[0]} and the last letter is {my_string[my_string_length - 1]}")

# 2 print the string
sub_string = ""
for i in range(my_string_length):
    sub_string += my_string[i]
    print(sub_string)

# 3 shuffle the string
my_string_to_list = list(my_string)
random.shuffle(my_string_to_list)
my_string = "".join(my_string_to_list)
print(my_string)