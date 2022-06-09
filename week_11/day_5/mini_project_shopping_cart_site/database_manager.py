import json


def create_database(dst_file='./data/products.json'):
    data = dst_file


def load_database(src_file='./data/products.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj)
    return data

