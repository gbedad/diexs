from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, DateField, DateTimeField, SelectField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired


class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    release_date = StringField('Release date', validators=[DataRequired()])
    created_in_country = StringField('Created in ', validators=[DataRequired()])
    category = SelectField('Category')
    country = SelectField('Country')
    #available_in_countries = StringField('Available in ')

    submit = SubmitField('Add Film')


class AddDirectorForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    film = SelectField('Film')

    submit = SubmitField('Add Director')
