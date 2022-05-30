# Exercise 1
# import datetime
from datetime import *
import holidays
import random
import string
from faker import Faker

import func

from func import add_func

from func import add_func as a_f

a_f(109, 367)
add_func(89, 45)

func.add_func(9, 34)

# Exercise 2


def guess_random():
    num = int(input("Enter a number between 1 and 100: "))
    if num == random.randint(1, 100):
        print("Same number, great!")


guess_random()

# Exercise 3

letters = string.ascii_letters
list_letters = list(letters)
random.shuffle(list_letters)
letters_5 = "".join(list_letters[0:5])

print(f"Random string of length {len(letters_5)} letters:", letters_5)


# Exercise 4 Current Date

def time_until_january_first():
    date_today = datetime.now()
    time_until = datetime(date_today.year + 1, 1, 1) - date_today
    return f"The 1st of January is in {time_until} hours"


print(time_until_january_first())


# Exercise 6 Birthday And Minutes

def minutes_of_life():
    string_date = input("Enter birthdate dd/mm/yyyy: ")
    dt = datetime.strptime(string_date, "%d/%m/%Y")
    # print(dt)
    d_today = datetime.now()
    delta_time_min = d_today - dt
    delta = delta_time_min.days * 24 * 60 + delta_time_min.seconds/60
    return f"From your birthdate {string_date} until today, you  have lived {delta} minutes"


result = minutes_of_life()
print(result)

# Exercise 7 Upcoming Holiday

def upcoming_holiday():
    dt1 = date.today()

    list_holidays = []
    for date_h in holidays.France(years=2022).items():

        if date_h[0] > dt1:
            list_holidays.append(((date_h[0] - dt1).days, date_h[1]))
    min_days = list_holidays[0][0]
    for i in range(len(list_holidays)):
        if list_holidays[i][0] < min_days:
            min_days = list_holidays[i][0]
            next_holiday = list_holidays[i]
            return f"Today is {dt1} and next holiday is '{next_holiday[1]}' in {next_holiday[0]} days"


print(upcoming_holiday())

# Exercise 8 : How Old Are You On Jupiter?
earth_days = 31557600
orbital_period = {"Earth": 1,
                  "Venus": 0.61519726,
                  "Mercury": 0.2408467,
                  "Mars": 1.8808158,
                  "Jupiter": 11.862615,
                  "Saturn": 29.447498,
                  "Uranus": 84.016846,
                  "Neptune": 164.79132}

def how_old_on_planet():
    time_in_seconds = int(input("Enter how seconds old "))
    for k, v in orbital_period.items():
        print(f"You are {v*time_in_seconds/earth_days: .2f} Earth-years old on {k}")

how_old_on_planet()


# Exercise 9 Faker Module

fake = Faker()

users = []


def add_user():
    users.append({"name": fake.name(), "address": fake.address(), "language_code": fake.language_code()})


add_user()
add_user()
add_user()
add_user()
add_user()

print(users)
for user in users:
    print(user)

