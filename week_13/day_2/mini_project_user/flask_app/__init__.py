import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

robots_app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
robots_app.config['SECRET_KEY'] = 'simplefornow'
robots_app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///" + os.path.join(basedir, 'robots.db')
robots_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(robots_app)
migrate = Migrate(robots_app, db)

from flask_app import models, routes, forms

"""
@robots_app.before_first_request
def populate():
    with open('/Users/geraldberrebi/Documents/DeveloperInstitute/diexs/week_13/day_2/mini_project_user/flask_app/users.json', 'r') as jsonfile:
        json_object = json.load(jsonfile)
        for user in json_object:
            model = models.User(name=user["name"], street=user["address"]["street"], city=user["address"]["city"],
                                zipcode=user["address"]["zipcode"])
            db.session.add(model)
            db.session.commit()
"""


