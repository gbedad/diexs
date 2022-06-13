import flask
from app_city import get_secret

web_app = flask.Flask(__name__)
web_app.config['SECRET_KEY'] = get_secret.SECRET_KEY

from app_city import routes, forms