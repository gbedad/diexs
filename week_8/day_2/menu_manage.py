# Exercise 3: Restaurant Menu Manager

class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        dish = {}
        dish["name"] = name
        dish["price"] = price
        dish["spice"] = spice
        dish["gluten"] = gluten
        self.menu.append(dish)
        print(self.menu)

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if name in item.values():
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
            elif name not in item.values():
                print(f"The dish {name} is not in the menu")

    def remove_item(self, name):
        for item in self.menu:
            if name in item.values():
                self.menu.remove(item)
                print(f"The dish {name} was removed from menu")
                print(self.menu)
            else:
                print(f"The dish {name} is not in menu")


tofoli = MenuManager()
tofoli.add_item(name="Soup", price=10, spice="B", gluten=False)
tofoli.add_item("Hamburger", 15, "A", True)

tofoli.update_item("Hamburger", 17, "A", False)
tofoli.update_item("Chicken", 17, "A", False)
# tofoli.add_item("Hamburger", 15, "A", True)

tofoli.remove_item("Hamburger")
tofoli.remove_item("Chicken")

