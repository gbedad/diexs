# Exercise 1 : Box Of Stars
# Instructions
# Write a function named box_printer that takes any amount of strings
# (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
# will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

# transform string in list
def transform_to_tuple(string):
    return tuple(string)


# Find the longest word
def find_longest(word_list):
    word_len = []
    for word in word_list:
        word_len.append(len(word))
    return max(word_len) + 4


# Complete line with stars
def stars_line(num):
    print("*" * num)


# Determine remaining spaces
def remaining_spaces(word, max_len):
    remainder = max_len - len(word) - 4
    return remainder


def box_printer(*words_tuple):
    words_to_tuple = transform_to_tuple(words_tuple)
    longest = find_longest(words_to_tuple)
    stars_line(longest)
    for word in words_tuple:
        print("* " + word + " " * remaining_spaces(word, longest) + " *")
    stars_line(longest)


box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# Sort in ascendant order
def insertion_sort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
