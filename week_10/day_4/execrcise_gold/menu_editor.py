import menu_manager


def load_manager():
    """
    This function will create a new MenuManager instance.
    """
    menu = menu_manager.MenuManager()
    return menu


def add_item_to_menu():
    print("Add item to menu")
    menu = load_manager()
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price: "))
    menu.add_item(item_name, item_price)
    menu.save_to_file()


def remove_item_from_menu():
    print("Delete item from menu")
    menu = load_manager()
    item_name = input("Enter the name  of the item to remove")
    menu.remove_item(item_name)
    menu.save_to_file()


def show_restaurant_menu():
    menu = load_manager().menu
    print("Menu")
    for item in menu["items"]:
        print(item)


def show_user_menu():
    """
    This function should display the program menu (not the restaurant menu!),
    and ask the user to choose an item. Call the appropriate function that
    matches the user’s input.
    :return: function called
    """
    print("""
    MENU
(a) Add an item
(b) Delete an item
(v) View the menu
(x) Exit 
    """)
    show = True
    while show:
        user_input = input("Select the option: ")
        user_input = user_input.lower()
        if user_input == 'a':
            add_item_to_menu()
        elif user_input == 'b':
            remove_item_from_menu()
        elif user_input == 'v':
            show_restaurant_menu()
        elif user_input == 'x':
            show = False
        else:
            print("Wrong input")


show_user_menu()


