from flask import Blueprint

film_blueprint = Blueprint('film', __name__, template_folder='templates', url_prefix='/film')

from app.film import routes
