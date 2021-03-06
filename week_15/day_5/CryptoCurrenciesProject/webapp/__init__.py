import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
from flask_bcrypt import Bcrypt
import os
import flask_mail
from os import getenv
import babel
import dateutil.parser
from babel.numbers import format_currency


from dotenv import load_dotenv

load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = getenv("EMAIL_USER", None)
app.config['MAIL_PASSWORD'] = getenv("EMAIL_PASS", None)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

login_mngr = flask_login.LoginManager(app)
login_mngr.login_view = 'login'
login_mngr.login_message_category = 'info'
bcrypt = Bcrypt(app)

mail = flask_mail.Mail(app)


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%b %d, %Y'
    return native.strftime(format)


@app.template_filter()
def usdollar(value):
    return format_currency(value, 'USD', locale='en_US')


from webapp import routes, models, forms
