import flask
import flask_sqlalchemy
import flask_migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))


from app.film import film_blueprint

flask_app = flask.Flask(__name__)

flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'flask_app.db')

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate(flask_app, db)

