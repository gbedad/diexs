import json


class MenuManager:
    def __init__(self):
        with open('restaurant_menu.json', 'r') as file_obj:
            self.menu = json.load(file_obj)

    def add_item(self, name, price):
        self.menu["items"].append({"name": name, "price": price})

    def remove_item(self, name):
        removed = False
        for item in self.menu["items"]:
            if item["name"] == name:
                self.menu["items"].remove(item)
                removed = True
        if removed:
            print(f"{name} removed from menu")
        else:
            print(f"This item '{name}' is not in the menu")

    def save_to_file(self):
        with open('restaurant_menu.json', 'w', encoding='utf-8') as f:
            json.dump(self.menu, f, indent=4)


menu1 = MenuManager()
# menu1.add_item(name="Fish", price=21)
menu1.remove_item("Fish")

menu1.save_to_file()
