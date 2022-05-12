# Exercise 1 double dice
# Create a function that will simulate the rolling of a dice.
# Call it throw_dice. It should return an integer between 1 and 6.

from random import randint


def throw_dice():
    return randint(1, 6)


# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they
# both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the
# dice in total. In the example above, it should return 3.

def throw_until_doubles():
    dice1 = throw_dice()
    dice2 = throw_dice()
    throws = [(dice1, dice2)]
    while dice1 != dice2:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throw = (dice1, dice2)
        throws.append(throw)
    return len(throws)


# print(throw_until_doubles())

# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times),
# and store the results of those function calls (in other words, how many throws it took
# until doubles were thrown, each time) in a collection. (What kind of collection?
# Read below to understand what we will need the data for,
# and this should help you decide which data structure to use).

def main():
    freq = {}
    count = 0
    i = 1
    while count <= 100:
        freq[i] = throw_until_doubles()
        count += freq[i]
        i += 1
    print(freq)
    return {"throws": i - 1, "average": round(count / (i - 1), 2)}

result = main()
print(f"The average of throws is {result['average']} on a total of {result['throws']} throws ")

