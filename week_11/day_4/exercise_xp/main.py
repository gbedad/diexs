import flask
from flask import render_template, url_for
import database_manager

app = flask.Flask(__name__)
database_manager.create_database()


@app.route("/")
def home_page():
    return render_template("homepage.html")


@app.route("/products")
def products_page():
    data = database_manager.load_database()
    # css = open('static/style.css', 'r').read()
    # return flask.render_template("my_template.html", products=data, additional_css=css)

    return render_template("products.html", products=data)


@app.route("/product/<product_id>")
def product_page(product_id):
    data = database_manager.load_database()

    for item in data:
        if item['ProductId'] == product_id:
            product = item
            break
    else:
        product = None

    # css = open('static/style.css', 'r').read()
    # return flask.render_template("my_template.html", products=data, additional_css=css)

    return render_template("product.html", product=product)


if __name__ == "__main__":
    app.run(debug=True, port=5500)