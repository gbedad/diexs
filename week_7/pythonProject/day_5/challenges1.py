# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.
import math

from functools import reduce


my_list = [4, 6, 45, 6]


def insert_item(list_items, value, position):
    new_list = []
    if position <= len(list_items):
        new_list = list_items[0:position] + [value] + my_list[position: len(list_items)]
    else:
        new_list = my_list
        print("Index out of range")

    return new_list


result = insert_item(my_list, 123, 3)

print(result)


# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.


def count_spaces(string):
    count = 0
    for char in string:
        if ord(char) == 32:
            count += 1
    if count == 0:
        count = 0
    return count


spaces = count_spaces("Write a script that counts the number of spaces in a string")
print(f"There are {spaces} spaces in the string.")


# Exercise 3
# Instructions
# Write a script that calculates the number of upper case
# letters and lower case letters in a string.


def is_upper(char):
    if char == char.upper() and ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
        return True
    else:
        return False


def calc_upper_lower(sentence):
    lowers = 0
    uppers = 0
    for letter in sentence:
        if is_upper(letter):
            uppers += 1
        else:
            lowers += 1
    return uppers, lowers


upper, lower = calc_upper_lower("Write A scRipt TO be in tHe lOOp")
print(f"Number of uppers is {upper} and number of lowers is {lower}")


# Exercise 4
# Instructions
# Write a function to find the sum of an array without using
# the built in function:


def my_sum(list_param):
    sum_list = 0
    for i in range(len(list_param)):
        sum_list += list_param[i]
    return sum_list


print(my_sum([1, 5, 4, 2]))


# Exercise 5
# Instructions
# Write a function to find the max number in a list


def find_max(list_param):
    max_num = list_param[0]
    for i in range(1, len(list_param)):
        if list_param[i] > max_num:
            max_num = list_param[i]
    return max_num


print(find_max([0, 1, 3, 50]))


# Exercise 6
# Instructions
# Write a function that returns factorial of a number


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(12))


# Exercise 7
# Instructions
# Write a function that counts an element
# in a list (without using the count method):
# list_count(['a','a','t','o'],'a')

def list_count(list_param, key):
    count = 0
    for item in list_param:
        if item == key:
            count += 1
    return count


print(list_count(['a', 'a', 't', 'o'], 'a'))

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares)
# of the sum of a list:
#     >>>norm([1,2,2])
#     >>>3


def norm(list_param):
    squared_norm = 0
    for num in list_param:
        squared_norm += num**2
    return math.sqrt(squared_norm)


print(norm([1, 2, 2]))


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic
# (sorted either ascending of descending)
#     >>>is_mono([7,6,5,5,2,0])
#     >>>True
#     >>>is_mono([2,3,3,3])
#     >>>True
#     >>>is_mono([1,2,0,4])
#     >>>False

def is_mono(list_param):
    if list_param  == sorted(list_param) or list_param == sorted(list_param, reverse=True):
        return True
    else:
        return False

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))

# Exercise 10 Write a function that prints the longest word in a list.


def longuest_word(list_param):
    maximum = list_param[0]
    for i in range(len(list_param)-1):
        if len(list_param[i+1]) > len(maximum):
            maximum = list_param[i+1]
    return maximum

sentence = "Write a function that prints the longest word in a list".split(' ')
print(sentence)
print(longuest_word(sentence))

# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list,
# and all the strings in another one.

# Exercise 12 Palidrome


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome('radar'))
print(is_palindrome('John'))

# Exercise 13 Write a function that returns the amount of words
# in a sentence with length > k:
#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3

def sum_over_k(sentence, k):
    count = 0
    sentence_to_list = sentence.split(" ")
    for word in sentence_to_list:
        if len(word) > k:
            count += 1
    return count

sentence = 'Do or do not there is no try'
k = 2
print(sum_over_k(sentence, k))


# Exercise 14 Write a function that returns the average value
# in a dictionary (assume the values are numeric):
#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3

def dict_avg(dict_param):
    sum_values = 0
    items = 0
    for key, value in dict_param.items():
        sum_values += value
        items += 1
    return sum_values / items


print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))

# Exercise 15 Write a function that returns common divisors of 2 numbers:
#     >>>common_div(10,20)
#     >>>[2,5,10]


def common_div(num1, num2):
    divisors = []
    lower_num = min(num1, num2)
    higher_num = max(num1, num2)
    for i in range(2, lower_num+1):
        if lower_num % i == 0 and higher_num % i == 0:
            divisors.append(i)
    return divisors

print(common_div(30, 60))


# Exercise 16
# Instructions
# Write a function that test if a number is prime.
#     >>>is_prime(11)
#     >>>True
def is_prime(num):
    divisors = []
    for i in range(2, num):
        if num % i == 0:
            divisors.append(num)
    if len(divisors) == 0:
        return True
    else:
        return False

print(is_prime(23))

# Exercise 17
# Instructions
# Write a function that prints elements of a list
# if the index and the value are even:
#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]


def weird_print(list_param):
    weird_list = []
    for i in range(len(list_param)):
        if i % 2 == 0 and list_param[i] % 2 == 0:
            weird_list.append(list_param[i])
    return weird_list


print(weird_print([1,2,2,3,4,5]))


# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded
# arguments and return the count of different types:
#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2

def type_count(**kwargs):
    type_values = {}
    values_list = []
    freq = {}
    for key, value in kwargs.items():
        type_values[key] = type(value)
    for value in type_values.values():
        values_list.append(value)
    for item  in values_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


print(type_count(a=1,b='string',c=1.0,d=True,e=False))


# Exercise 19 mimics the split function

print("word/show".split("/"))


def split_mimic(string_param, separator=' '):
    list_param = []
    for i in range(len(string_param)):
        if string_param[i] == separator:
            list_param.append(string_param[:i])
            i += 1
    return list_param
print(split_mimic("word show again", " "))



# Exercise 20 Convert a string into password format

def convert_to_password(word):
    print('*'*len(word))

convert_to_password(word="mypassword")



