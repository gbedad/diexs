"""
Instructions
Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
Display a little cake as seen below:
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

Bonus : If they were born on a leap year, display two cakes !
"""

from datetime import date
import math
birth_date = input("Enter your birth date DD/MM/YYYY : ")
# convert to date format
day_birth = int(birth_date[0:2])
month_birth = int(birth_date[3:5])
year_birth = int(birth_date[6:])

# Define date of the day
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
day_today = int(d1[0:2])
month_today = int(d1[3:5])
year_today = int(d1[6:])

f_date = date(year_birth, month_birth, day_birth)
l_date = date(year_today, month_today, day_today)
delta = l_date - f_date
print(int(delta.days/365))
age = int(delta.days/365)


# Assign immutable part of the cake to a variable
cake = """
   |:H:a:p:p:y:|
 __|___________|__
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~
"""
# Define the unit value of the age using modf included python function
extract_units = math.modf(age / 10)
unit = int(extract_units[0]*10)
# print(int(est_units[0]*10))
# Calculate the number of candles
if unit == 0:
    unit = 10

left = int((11 - unit)/2)
right = 11 - (left + unit)
lines = int((11 - unit)/2)
candles = '    '+'_'*left+'i'*unit+'_'*right + cake
# print(candles)

# Bonus if it is a leap year display 2 cakes


# century year divided by 400 is leap year
if (year_birth % 400 == 0) and (year_birth % 100 == 0):
    leap_year = True
    print("{0} is a leap year".format(year_birth))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year_birth % 4 == 0) and (year_birth % 100 != 0):
    leap_year = True

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    leap_year = False

cakes = candles*2 if leap_year else candles
print(cakes)




