# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)

# Exercise 2 : Cinemax #2
# Instructions
# “Continuation of Exercise Cinemax from Week4Day2 XP”
#
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Given the following object:
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# How much does each family member have to pay ?
#
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead
# of using the provided family variable (Hint: ask the user for
# names and ages and add them into a family dictionary that is initially empty).

total_price = 0
ticket_price = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key, value in family.items():
    if value < 3:
        ticket_price = 0
        print(f"{key} will pay ${ticket_price}")
        total_price += 0
    elif 3 <= value <= 12:
        ticket_price = 10
        print(f"{key} will pay ${ticket_price}")
        total_price += 10
    elif value > 12:
        ticket_price = 15
        print(f"{key} will pay ${ticket_price}")
        total_price += 15

print(f"The family will pay ${total_price}")

family_dict = {}
how_many = int(input("How many person ? "))
for person in range(how_many):
    user_input = input("Enter name and age comma-separated: ")
    family = user_input.split(",")
    family_dict[family[0]] = family[1]
print(family_dict)

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
#
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
#
# creation_date: 1975
# number_stores: 10 000
#
#
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

brand = {"name": "Zara", "creation_date": 1975, "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes": ["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"], "number_stores": 2,
         "major_color": {"France": ["blue"],
                         "Spain": ["red"],
                         "US": ["pink", "green"]
                         }}

print(brand)

print(f"The clients of {brand['name']} are {brand['type_of_clothes']} ")

key = "international_competitors"
if key in brand:
    brand[key].append("Desigual")
brand["country_of_creation"] = "Spain"
del brand["creation_date"]
competitors = brand["international_competitors"]
competitors_number = len(competitors)
print(competitors[competitors_number-1])
print(brand)
print(brand["major_color"]["US"])
print(len(brand))
print()
for key in brand.keys():
    print(key)
print()
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand["number_stores"])

# Exercise 4 : Disney Characters
# Instructions
# Use this list :
#
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
mickey_users1 = {}
for i in range(len(users)):
    mickey_users1[users[i]] = i
print(mickey_users1)

mickey_users2 = {}
for i in range(len(users)):
    mickey_users2[i] = users[i]
print(mickey_users2)

mickey_users3 = {}
sorted_users = sorted(users)
for i in range(len(sorted_users)):
    mickey_users3[sorted_users[i]] = i
print(mickey_users3)

mickey_users4 = {}
for i in range(len(users)):
    if "i" in users[i]:
        mickey_users4[users[i]] = i
print(mickey_users4)

mickey_users5 = {}
for i in range(len(users)):
    print(users[i])
    if users[i][0].lower() == "m" or users[i][0].lower() == "p":
        mickey_users5[users[i]] = i
print(mickey_users5)