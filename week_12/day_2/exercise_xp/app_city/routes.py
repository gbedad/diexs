import os.path

import flask
from flask import url_for, flash, request, redirect
from werkzeug.utils import secure_filename

from app_city.file_uploads import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from app_city.forms import AddCity
import json


from app_city import web_app, city_manager
file_cities = 'app_city/cities_around_the_world.json'
file_size = os.path.getsize(file_cities)

with open(file_cities, 'r+') as file_obj:
    if file_size == 0:
        list_of_cities = []
        json.dump(list_of_cities, file_obj)
    else:
        list_of_cities = json.load(file_obj)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@web_app.route("/", methods=("GET", "POST"))
def index():
    form = AddCity()
    if form.validate_on_submit():
        city_name = form.city_name.data
        country_name = form.country_name.data
        number_inhabitants = form.number_inhabitants.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        capital = form.is_capital.data
        city_area = form.city_area.data
        if request.method == 'POST':
            uploaded_file = request.files['picture']
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join(web_app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        city_data = {"City": city_name, "Country": country_name, "Population": number_inhabitants, "Surface": city_area,
                     "Latitude": latitude, "Longitude": longitude, "Capital": capital, "Picture": uploaded_file.filename}
        list_of_cities.append(city_data)
        city_manager.save_city_to_json(city_data)
        print(list_of_cities)
        print(f"city: {city_name}")
        print(f"country: {country_name}")
        print(f"inhabitants: {number_inhabitants}")
        print(f"area: {city_area}")

        return flask.redirect(url_for('home'))

    return flask.render_template("index.html", form=form)


@web_app.route('/home')
def home():
    return "Check"
