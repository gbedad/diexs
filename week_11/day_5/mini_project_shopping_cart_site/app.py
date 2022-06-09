from flask import Flask, url_for, render_template, redirect

import products_data

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
    added_product = list(products_data.retrieve_requested_product(product_id))[0]
    cart_item.append(added_product)
    print(cart_item)
    return redirect(url_for('cart', cart=cart_item))



if __name__ == "__main__":
    app.run(debug=True)

