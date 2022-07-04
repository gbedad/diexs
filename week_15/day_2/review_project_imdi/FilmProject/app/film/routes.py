from flask import render_template, redirect, url_for,  Blueprint
from app import db

from app.film.forms import *
from app.film.models import *

film = Blueprint('film', __name__, template_folder='templates', url_prefix='/films')


@film.route('/add_film', methods=['GET', 'POST'])
def add_film():

    form = AddFilmForm()

    if form.validate_on_submit():
        return redirect('homepage.html')

    return render_template('/film/addFilm.html', title='Add Film', form=form)


@film.route('/add_director', methods=['GET', 'POST'])
def add_director():
    form = AddDirectorForm()

    if form.validate_on_submit():
        new_director = Director(first_name=form.first_name.data, last_name=form.last_name.data, film=form.film.data)
        db.session.add(new_director)
        db.commit()

        return redirect(url_for('add_director'))

    return render_template('/director/addDirector.html', title='Add Director', form=form, legend='Add Director')



