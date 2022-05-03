# Exercise 1: Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius),
# selected at random.
# Test your function to make sure it generates expected results.
import random


# def get_random_temp():
#     temp = random.randint(-10, 41)
#     return temp


# my_temp = get_random_temp()
# print(my_temp)


# Create a function called main().
# Inside this function, call get_random_temp()
# to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message,
# eg. “The temperature right now is 32 degrees Celsius.”

# def main():
#     my_temp = get_random_temp()
#     print(f"The temperature right now is {my_temp} degrees Celsius.")
#
#
# main()

# Let’s add more functionality to the main() function.
# Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40


# def main():
#     my_temp = get_random_temp()
#     print(f"The temperature right now is {my_temp} degrees Celsius.")
#     if my_temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= my_temp < 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif 16 <= my_temp < 24:
#         print("Not too bad, I don't need a coat.")
#     elif 24 <= my_temp < 32:
#         print("It is almost summer!")
#     else:
#         print("Take care, the sun is too strong!")
#
#
# main()


# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number
# between -10 and 40, set lower and upper limits based on the season,
# eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season,
# so that we can call the function correctly. Ask the user to type
# in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer),
# ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

def determine_season(month):
    if 12 <= month < 3:
        return "winter"
    elif 3 <= month < 6:
        return "spring"
    elif 6 <= month < 9:
        return "summer"
    elif 9 <= month < 12:
        return "fall"


def get_random_temp(season):
    """Improved function with params season"""
    if season == "spring":
        return round(random.uniform(18, 25), 1)
    elif season == "summer":
        return round(random.uniform(25, 41), 1)
    elif season == "fall":
        return round(random.uniform(5, 18), 1)
    elif season == "winter":
        return round(random.uniform(-10, 5), 1)


def main():
    get_month = int(input("What is the month? "))
    get_season = determine_season(get_month)
    my_temp = get_random_temp(get_season)
    print(f"The season is {get_season} and the temperature right now is {my_temp} degrees Celsius.")
    if my_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= my_temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= my_temp < 24:
        print("Not too bad, I don't need a coat.")
    elif 24 <= my_temp < 32:
        print("I like summer!")
    else:
        print("Take care, the sun is too strong!")


main()