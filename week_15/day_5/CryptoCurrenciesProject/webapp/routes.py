from webapp import app
from webapp.models import Cryptocurrencies, User
from flask import render_template_string, render_template, redirect, url_for, flash
from webapp import forms
from flask_login import login_user, current_user, logout_user, login_required
from webapp import db, bcrypt


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '91f90390-6831-4e62-b62e-824b6d76ae02',
}

session = Session()
session.headers.update(headers)
"""
try:
    response = session.get(url)
    data = json.loads(response.text)
    all_currencies = data["data"]
    print(all_currencies)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
"""


@app.route('/')
def index():
    filtered_currencies = []
    cryptos = Cryptocurrencies.query.all()
    '''for crypto in cryptos:
        url_id = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        try:
            response = session.get(url_id, params=parameters)
            data = json.loads(response.text)["data"]
            all_currencies = [x for x in data if x["id"] == crypto.id]
            filtered_currencies.append(all_currencies[0])
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        print(crypto.id)'''
    return render_template("index.html", values=cryptos)


@app.route('/currency/<int:crypto_id>', methods=['GET', 'POST'])
def get_currency(crypto_id):
    #crypto_id = Cryptocurrencies.get_info()
    print(crypto_id)
    parameters = {
        'id': crypto_id
    }
    url_id = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    try:
        response = session.get(url_id, params=parameters)
        data = json.loads(response.text)["data"]
        print(data[str(crypto_id)])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    return render_template("specifics.html", crypto=data, selected_id=str(crypto_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = forms.RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password, email=form.email.data,
                    fullname=form.fullname.data)
        db.session.add(user)

        db.session.commit()
        flash('Registered to an existing team', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form, legend='Registration Form')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: # Check if the user is not already logged in
        return redirect(url_for('index'))

    form = forms.LoginForm() # Load the form

    if form.validate_on_submit():
        # Retrieve the user with the username
        user = User.query.filter_by(username=form.username.data).first()

        # Check if it exist and if the password is the right password
        if user is None or not user.password == form.password.data:
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # Log the user in
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form) # Render the form


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
