import flask_wtf
import wtforms


class AddUser(flask_wtf.FlaskForm):
    user_name = wtforms.StringField("Name")
    street = wtforms.StringField("Street")
    city = wtforms.StringField("City")
    zipcode = wtforms.StringField("Zipcode")
    submit = wtforms.SubmitField("Submit")


class Login(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name")
    city = wtforms.StringField("City")

    submit = wtforms.SubmitField("Submit")


