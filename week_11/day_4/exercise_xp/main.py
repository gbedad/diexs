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


@app.route("/products/<product_id>")
def product_page(product_id):
    data = database_manager.load_database()
    filtered = filter(lambda x: x["ProductId"] == product_id, data)
    product = list(filtered)[0]

    # for item in data:
    #     if item['ProductId'] == product_id:
    #         product = item
    #         break
    # else:
    #     product = None

    # css = open('static/style.css', 'r').read()
    # return flask.render_template("my_template.html", products=data, additional_css=css)

    return render_template("product.html", product=product)


@app.route('/products/search/by-category/<string:category_name>') # as we menthened this string is redundant
def search_by_category(category_name):
    data = database_manager.load_database()
    filtered = filter(lambda x: x["Category"] == category_name, data)
    return render_template('search-by-category.html', products=list(filtered), category=category_name)


@app.route('/products/search/by-name/<string:product_name>')
def search_by_name(product_name):
    data = database_manager.load_database()
    filtered = filter(lambda x: product_name in x["Name"], data)
    return render_template('search-by-name.html', products=list(filtered), name=product_name)


if __name__ == "__main__":
    app.run(debug=True, port=5500)
