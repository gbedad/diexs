import collections
import math
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers,
# use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:
#
# 18,22,24
C = 50
H = 30
user_input = input("Enter a comma-separated string of numbers: ")
d = user_input.split(",")
d_tuple = tuple(d)
q_list = []
for D in d_tuple:
    Q = math.sqrt((2 * C * int(D))/H)
    q_list.append(int(Q))
q_tuple = tuple(q_list)
print(q_tuple)

# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:
#
#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.
# Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers
# A list containing the first and the last numbers.
# A list of all the numbers greater than 50.
# A list of all the numbers smaller than 10.
# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# The numbers without any duplicates – also print how many numbers are in the new list.
# The average of all the numbers.
# The largest number
# 10.The smallest number.
# 11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
# 12.Extra bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers
# between -100 and 100.
# Ask the user for an integer between -100 and 100 –
# repeat this question 10 times. Each number should be added
# into a variable that you created earlier.

a = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
b = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
c = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
d = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# for num in a:
#     print(num)
# for num in b:
#     print(num)
# for num in c:
#     print(num)
# for num in d:
#     print(num)
print(sorted(a)[::-1])
print(sorted(b))
print(sorted(c))
print(sorted(d))
print(sum(a))
print(a[0], a[len(a)-1])

list_bigger_50 = []
for num in a:
    if num >= 50:
        list_bigger_50.append(num)
for num in b:
    if num >= 50:
        list_bigger_50.append(num)
for num in c:
    if num >= 50:
        list_bigger_50.append(num)
for num in d:
    if num >= 50:
        list_bigger_50.append(num)
print(list_bigger_50)

list_smaller_10 = []
for num in a:
    if num <= 10:
        list_smaller_10.append(num)
for num in b:
    if num <= 10:
        list_smaller_10.append(num)
for num in c:
    if num <= 10:
        list_smaller_10.append(num)
for num in d:
    if num <= 10:
        list_smaller_10.append(num)
print(list_smaller_10)

result = map(lambda x: x * x, a)
print(list(result))
b_without_duplicate = list(set(b))
print(b_without_duplicate)

print(max(c))
print(min(c))

average_a = sum(a) / len(a)
print(f"The average of a is {average_a}.")

# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

paragraph = "A dictionary is a valuable data structure in Python; it holds key-value pairs. During programming, there is often a need to extract the value of a given key from a dictionary; however,it is not always guaranteed that a specific key exists in the dictionaryHence, it is a safe practice to check whether or not the key exists in the dictionary prior to extracting the value of that key. For that purpose, Python offers two built-in functions:The has_key method returns true if a given key is available in the dictionary; otherwise, it returns false.This approach uses the if-in statement to check whether or not a given key exists in the dictionary."


print(f"This paragraph contain {len(paragraph)} characters.")
sentences = paragraph.split(".")
print(f"The paragraph contain {len(sentences)} sentences")
words = paragraph.split(" ")
unique_words = set(words)
print(f"The paragraph is composed with {len(words)} words and {len(unique_words)} unique words..")
white_space = ord(" ")
print(white_space)
letter_count = 0
for letter in paragraph:
    if ord(letter) != 32:
        letter_count += 1
print(letter_count)
average_words_in_sentence = len(words) / len(sentences)
print(average_words_in_sentence)
print(words)

freq = {}
non_unique_words_counter = 0
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
for key, value in freq.items():
    if value > 1:
        non_unique_words_counter += 1
    print(f"{key}: {value}")
print(f"There are {non_unique_words_counter} non unique words.")

# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.
#
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#
# Then, the output should be:

phrase = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
phrase_list = phrase.split(" ")
print(phrase_list)
frq = {}
for w in phrase_list:
    if w in frq:
        frq[w] += 1
    else:
        frq[w] = 1

for k, v in frq.items():
    print(f"{k}: {v}")
