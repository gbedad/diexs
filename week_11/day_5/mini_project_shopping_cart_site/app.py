from flask import Flask, url_for, render_template, redirect

import products_data
import cart_manager

app = Flask(__name__)


cart_item =[]


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/products')
def products():
    data = products_data.retrieve_all_products()
    return render_template('products.html', products=data)


@app.route('/products/<product_id>')
def product(product_id):
    prod = list(products_data.retrieve_requested_product(product_id=product_id))
    requested_prod = dict(prod[0])
    print(requested_prod["ProductId"])
    return render_template('product.html', product=requested_prod)


@app.route('/cart')
def cart():
    total = 0
    my_cart = cart_item
    for item in cart_item:
        total += item["Price"]

    return render_template('cart.html', cart=my_cart, total=total)


@app.route('/add_product_to_cart/<product_id>')
def add_to_cart(product_id):
    added_product_full = list(products_data.retrieve_requested_product(product_id))[0]
    added_product = {"ProductId": added_product_full["ProductId"], "Name": added_product_full["Name"], "Price": added_product_full["Price"]}
    cart_item.append(added_product)
    print(cart_item)
    # cart_manager.save_cart_to_json(cart_item)
    return redirect(url_for('cart', cart=cart_item))


@app.route('/delete_product_from_cart/<product_id>')
def delete_from_cart(product_id):
    deleted_item = list(products_data.retrieve_requested_product(product_id))[0]
    cart_item.remove(deleted_item)
    print(cart_item)
    # cart_manager.save_cart_to_json(cart_item)
    return redirect(url_for('cart', cart=cart_item))


@app.route('/save_cart')
def save_cart():
    cart_manager.save_cart_to_json(cart_item)
    return redirect(url_for('products'))


if __name__ == "__main__":
    app.run(debug=True)

