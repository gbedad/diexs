import flask_wtf
import wtforms
from wtforms.validators import ValidationError
from flask_app.models import User


class AddUser(flask_wtf.FlaskForm):
    user_name = wtforms.StringField("Name")
    street = wtforms.StringField("Street")
    city = wtforms.StringField("City")
    zipcode = wtforms.StringField("Zipcode")
    submit = wtforms.SubmitField("Add User")

    def validate_name(self, user_name):
        user = User.query.filter_by(name=user_name.data).first()
        print(user)
        if user:
            raise ValidationError('User already existing')


class Login(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name")
    city = wtforms.StringField("City")

    submit = wtforms.SubmitField("Login")




