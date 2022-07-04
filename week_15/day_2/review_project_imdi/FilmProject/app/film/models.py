from app import db
from datetime import date


country_table = db.Table('countries',
                         db.Column('film_id', db.Integer, db.ForeignKey('film.id)')),
                         db.Column('country_id', db.Integer, db.ForeignKey('country.id')))


category_table = db.Table('categories',
                          db.Column('film_id', db.Integer, db.ForeignKey('film.id)')),
                          db.Column('category_id', db.Integer, db.ForeignKey('category.id')))


director_table = db.Table('directors',
                          db.Column('film_id', db.Integer, db.ForeignKey('film.id)')),
                          db.Column('director_id', db.Integer, db.ForeignKey('director.id')))


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    films = db.relationship('Film', backref='country', lazy='dynamic')

    def __repr__(self):
        return f'<Country: {self.name}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return f'<Category: {self.name}'


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64))
    release_date = db.Column(db.Date, default=date.today())
    created_in_country = db.Column(db.String(64), db.ForeignKey('country.id'))
    available_in_countries = db.relationship('Country', secondary=country_table, backref=db.backref('country', lazy='dynamic'))
    category = db.relationship('Category', secondary=category_table)
    director = db.relationship('Director', secondary=director_table)

    def __repr__(self):
        return f'<Film: {self.title}'


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Director: {self.first_name} {self.last_name}'



