from flask import render_template, redirect, url_for,  Blueprint

from app.film import film_blueprint


@film_blueprint.route('/homepage')
def home():
    return render_template('homepage.html')

