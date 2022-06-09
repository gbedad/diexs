import database_manager

database_manager.create_database()


def retrieve_all_products():
    data = database_manager.load_database()
    all_products = data
    return all_products


def retrieve_requested_product(product_id):
    products = retrieve_all_products()
    requested_product = filter(lambda x: x["ProductId"] == product_id, products)
    return requested_product


# retrieve_all_products()

# print(retrieve_requested_product('HT-1003'))


