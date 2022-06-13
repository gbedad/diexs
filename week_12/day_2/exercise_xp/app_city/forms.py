import flask_wtf
import wtforms


class AddCity(flask_wtf.FlaskForm):
    city_name = wtforms.StringField("City Name")
    country_name = wtforms.StringField("Country")
    number_inhabitants = wtforms.IntegerField("Inhabitants")
    city_area = wtforms.IntegerField("City area")
    add_city = wtforms.SubmitField("Add City")

