import flask
from flask import url_for
from app_city.forms import AddCity

from app_city import web_app, city_manager

list_of_cities = []


@web_app.route("/", methods=("GET", "POST"))
def index():
    form = AddCity()
    if form.validate_on_submit():
        city_name = form.city_name.data
        country_name = form.country_name.data
        number_inhabitants = form.number_inhabitants.data
        city_area = form.city_area.data
        city_data = {"City": city_name, "Country": country_name, "Population": number_inhabitants, "Surface": city_area}
        list_of_cities.append(city_data)
        city_manager.save_city_to_json(list_of_cities)
        print(list_of_cities)
        print(f"city: {city_name}")
        print(f"country: {country_name}")
        print(f"inhabitants: {number_inhabitants}")
        print(f"area: {city_area}")

        return flask.redirect(url_for('index'))

    return flask.render_template("index.html", form=form)


@web_app.route('/home')
def home():
    return "Check"
