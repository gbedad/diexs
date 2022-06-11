from flask import Flask, url_for, render_template, redirect, flash, request, session
from forms import RegistrationForm, LoginForm
from flask_session import Session

import products_data, cart_manager, user_data


app = Flask(__name__)
app.config['SECRET_KEY'] = '8147d28eecb58f4b7f34e1f1f1b00fc0'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


cart_item =[]


@app.route('/')
def home():
    if not session.get("name"):
        return redirect("/login")
    return render_template('homepage.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = {"Username": form.username.data, "Password": form.password.data}
        print(new_user)
        user_data.add_user(new_user=new_user)
        flash(f"Account created from {form.username.data}", 'success')
        return redirect(url_for('home'))
    # username = input("Enter username: ")
    # password = input("Enter password: ")

    return render_template('signup.html', form=form, title='Sign Up')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        check_user = user_data.check_user(user=form.username.data, password=form.password.data)
        flash(f"Account created from {form.username.data}", 'Login successful')
        if not check_user:
            return redirect(url_for('signup'))
        else:
            if request.method == "POST":
                session["name"] = request.form.get("name")
                print(session["name"])
                return redirect(url_for('products'))
    return render_template('login.html', form=form, title="Login")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")


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
    return redirect(url_for('products'))


@app.route('/delete_product_from_cart/<product_id>')
def delete_from_cart(product_id):
    for item in cart_item:
        if item["ProductId"] == product_id:
            deleted_item = item
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

