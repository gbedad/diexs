# Exercise 1
birthdays = {
    "John": "1995/09/02",
    "Bob": "1990/12/04",
    "Anna": "2001/06/23",
    "Rachel": "1966/12/07",
    "Seth": "1075/03/22"
}
# Exercise 3
new_name = input("Enter a name: ")
new_birth_date = input("Enter a date YYYY/MM/DD: ")
updated = {new_name: new_birth_date}
birthdays.update(updated)

print("Hello, you can ask the date of birth of your friends")
user_input = input("Enter the name: ")
for key, value in birthdays.items():
    if key == user_input:
        print(f"The date of birth of {key} is {birthdays[key]}")
        break
else:
    print(f"Sorry, we don’t have the birthday information for {user_input}")

# Exercise 2
for key in birthdays.keys():
    print(key)

# Exercise 4
# Create a new dictionary called items and populate the dictionary with the following
# key value pairs, each pair represents an item and its price.
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# Print all the items and their prices in a sentence.
# Change the value of all the keys to dictionaries containing
# both the price and the amount of items in stock.
# Once you’ve added the stock details write some code
# to calculate how much it would cost to buy everything in stock.

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for k, v in items.items():
    print(k, v)

items_in_stock = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 8},
    "orange": {"price": 1.5, "stock": 13},
    "pear": {"price": 3, "stock": 4}
}
amount = 0
for i in items_in_stock:
    amount += items_in_stock[i]["price"] * items_in_stock[i]["stock"]
print(f"The total price for the stock is : ${amount}")

# print(items_in_stock["banana"]["stock"]*items_in_stock["banana"]["price"])
print()


# Exercise 5
str_cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = str_cars.split(",")
sorted_cars_list = sorted(cars_list)

print(f"There is {len(cars_list)} manufacturers in the list")
print(sorted_cars_list[::-1])

cars = []
for car in sorted_cars_list:
    if "o" in car:
        cars.append(car)
print(f"There are {len(cars)} brands with letter o in the list")

cars_i = []
for car in sorted_cars_list:
    if "i" not in car:
        cars_i.append(car)
print(f"There are {len(cars_i)} brands without letter i in the list")

new_car_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
car_list_wo_duplicate = set(new_car_list)
print(list(car_list_wo_duplicate))
str_cars_list = ",".join(list(car_list_wo_duplicate))
print(str_cars_list)
print(f"There are {len(list(car_list_wo_duplicate))} manufacturers in the list.")
sorted_list = sorted(list(car_list_wo_duplicate))
print(sorted_list)
r_sorted_list = []
for car in sorted_list:
    r_car = ""
    for i in range(len(car)-1, -1, -1):
        r_car += car[i]
    r_sorted_list.append(r_car)
print(r_sorted_list)

