import json


def save_cart_to_json(cart):
    json_cart_file = "cart_item.json"
    with open(json_cart_file, "w") as file_obj:
        json.dump(cart, file_obj, indent=2)
    return json_cart_file

