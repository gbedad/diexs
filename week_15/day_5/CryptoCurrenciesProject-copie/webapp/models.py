from webapp import db, login_mngr, app
from flask_login import UserMixin
from itsdangerous import TimedSerializer as Serializer
from sqlalchemy.dialects.postgresql import JSON
import time
import jwt


@login_mngr.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


cryptocurrencies_table = db.Table('currencies',
                                  db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                                  db.Column("crypto_id", db.Integer, db.ForeignKey("cryptocurrencies.id")))

users_table = db.Table('users',
                       db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                       db.Column("crypto_id", db.Integer, db.ForeignKey("cryptocurrencies.id")))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    currencies = db.relationship("Cryptocurrencies", secondary=cryptocurrencies_table, back_populates="users")

    '''def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['id']
        except:
            return None
        return User.query.get(user_id)'''

    def get_reset_password_token(self, expires_in=600):
        timeout = time.time() + expires_in
        payload = {
            'reset_password': self.id,
            'exp': timeout
        }

        # Get the secret key from config
        secret_key = app.config['SECRET_KEY']

        # Create the token
        token = jwt.encode(payload, secret_key, algorithm="HS256")

        # Turn it to string
        s_token = token

        return s_token

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def __repr__(self):
        return f'<User: {self.username}>'


class Cryptocurrencies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
    logo = db.Column(db.String(64))
    is_active = db.Column(db.Integer)
    users = db.relationship("User", secondary=cryptocurrencies_table, back_populates="currencies")

    def get_info(self):
        crypto = Cryptocurrencies.query.filter_by(self.id)
        return crypto

    def __repr__(self):
        return f'<Cryptocurrency: {self.name}>'
