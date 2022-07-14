import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
from flask_bcrypt import Bcrypt
import os


basedir = os.path.abspath(os.path.dirname(__file__))


app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

login_mngr = flask_login.LoginManager(app)
bcrypt = Bcrypt(app)


from webapp import routes, models, forms
