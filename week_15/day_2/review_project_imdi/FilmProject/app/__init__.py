import flask
import flask_sqlalchemy
import flask_migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))


flask_app = flask.Flask(__name__)

flask_app.config['SECRET_KEY'] = 'you-will-never-guess'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'flask_app.db')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app.film.routes import film

flask_app.register_blueprint(film)




