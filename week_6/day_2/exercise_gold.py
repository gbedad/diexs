# Exercise 1 : Hello World-I Love Python
print("Hello World\n"*4 + "I love Python\n"*4)

# Exercise 2 : What Is The Season ?

"""Instructions
Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)
"""
month = int(input("Enter the month: "))
print(f"Month = {month}")
if 3 <= month < 6:
    print("Spring runs from March (3) to May (5)")
elif 6 <= month < 9:
    print("Summer runs from June (6) to August (8)")
elif 9 <= month < 12:
    print("Autumn runs from September (9) to November (11)")
else:
    print("Winter runs from December (12) to February (2)")
