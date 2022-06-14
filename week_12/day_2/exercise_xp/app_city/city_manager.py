import json


def save_city_to_json(city, filename='app_city/cities_around_the_world.json'):
    with open(filename, 'r+') as file_obj:
        file_data = json.load(file_obj)
        assert isinstance(file_data, object)
        file_data.append(city)
        file_obj.seek(0)
        json.dump(file_data, file_obj, indent=2)


