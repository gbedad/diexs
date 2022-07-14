from webapp import db, login_mngr
from flask_login import UserMixin, login_manager


@login_mngr.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""cryptocurrencies_table = db.Table('currencies',
                                  db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                                  db.Column("crypto_id", db.Integer, db.ForeignKey("cryptocurrencies.id")))

users_table = db.Table('users',
                       db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                       db.Column("crypto_id", db.Integer, db.ForeignKey("cryptocurrencies.id")))"""


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    #currencies = db.relationship("Cryptocurrencies", secondary=cryptocurrencies_table, back_populates="user")

    def __repr__(self):
        return f'<User: {self.username}>'


class Cryptocurrencies(db.Model):
    __tablename__ = "cryptocurrencies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
    is_active = db.Column(db.Integer)
    #users = db.relationship("User", secondary=users_table, back_populates="cryptocurrencies")

    def get_info(self):
        crypto = Cryptocurrencies.query.filter_by(self.id)
        return crypto

    def __repr__(self):
        return f'<Cryptocurrency: {self.name}>'
