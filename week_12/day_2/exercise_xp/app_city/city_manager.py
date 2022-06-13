import json


def save_city_to_json(city):
    json_file = 'app_city/cities_around_the_world.json'
    with open(json_file, 'w+') as file_obj:
        json.dump(city, file_obj, indent=2)
    return json_file

