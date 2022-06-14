import flask_wtf
import wtforms
from wtforms.validators import DataRequired, Length


class PositiveIntegerValidator(object):
    def __init__(self, message=None):
        if not message:
            message = "Field must be a positive integer"
        self.message = message

    def __call__(self, form, field):
        if field.data < 0:
            raise ArithmeticError("Must be a  positive integer")


class AddCity(flask_wtf.FlaskForm):
    city_name = wtforms.StringField("City Name", validators=[DataRequired(), Length(max=15)])
    country_name = wtforms.StringField("Country", validators=[DataRequired()])
    number_inhabitants = wtforms.IntegerField("Inhabitants", validators=[DataRequired(), PositiveIntegerValidator()])
    city_area = wtforms.IntegerField("City area")
    latitude = wtforms.FloatField("Latitude")
    longitude = wtforms.FloatField("Longitude")
    is_capital = wtforms.BooleanField("Capital", false_values=(False, 'false', 0, '0'))
    add_city = wtforms.SubmitField("Add City")




