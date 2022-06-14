import flask
from app_city import get_secret, file_uploads

web_app = flask.Flask(__name__)
web_app.config['SECRET_KEY'] = get_secret.SECRET_KEY
web_app.config['UPLOAD_FOLDER'] = file_uploads.UPLOAD_FOLDER

from app_city import routes, forms