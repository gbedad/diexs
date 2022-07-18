from webapp import app, db, bcrypt, mail
from webapp.models import Cryptocurrencies, User
from flask import render_template, redirect, url_for, flash, request
from webapp import forms
from flask_login import login_user, current_user, logout_user, login_required
from webapp.mailing import send_email
from flask_mail import Message


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


@app.route('/currency/send_email')
@login_required
def send_email_info():
    coin_name = request.args.get('coin_name', None)
    symbol = request.args.get('symbol', None)
    description = request.args.get('description', None)
    user = current_user
    msg = Message(f'Information Request',
                  sender='noreply@gmail.com',
                  recipients=[user.email])
    msg.body = f'''Dear {user.username},
    Please find thereafter the requested information about {coin_name}:
    The symbol is: {symbol}
    Description: {description}.
    
    Yours,
    
    The CryptoCoins team
    '''
    mail.send(msg)
    flash('A message with the information has been sent. Check your email.', 'info')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = forms.RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        db.session.add(user)

        db.session.commit()
        flash('Your are now registred', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form, legend='Registration Form')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful, please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form, legend='Login Form')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def send_reset_email(user):
    token = user.get_reset_password_token()
    msg = Message('Password Reset Request',
                  sender='noreply@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('reset_token', token=token, _external=True)}
        If you did not make this request then simply ignore this email and no change will be made.
    '''
    mail.send(msg)


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            send_reset_email(user)

        flash('An email has been sent', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if user is None:
        flash('That is invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = forms.ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password

        db.session.commit()
        flash('Your password has been updated', 'success')
        return redirect(url_for('login'))

    return render_template('reset_token.html', title='Reset Password', form=form)


@app.route('/currency/add/<crypto_id>')
@login_required
def add_currency(crypto_id):
    user = current_user
    currency = Cryptocurrencies.query.filter_by(id=crypto_id).first()
    if currency in user.currencies:
        flash(f'{currency} already in portfolio', 'warning')
        return redirect(url_for('index'))

    user.currencies.append(currency)
    db.session.commit()
    flash(f'{currency} successfully added to your portfolio', 'info')

    return redirect(url_for('index'))


@app.route('/currencies/user')
@login_required
def show_user_currencies():
    user = current_user
    user_currencies = user.currencies

    return render_template('user_currencies.html', data=user_currencies,  title='User Currencies', legend='My Crypto Coins')


@app.route('/currency/delete/<crypto_id>')
@login_required
def delete_currency(crypto_id):
    user = current_user
    currency = Cryptocurrencies.query.filter_by(id=crypto_id).first()
    if currency not in user.currencies:
        flash(f'{currency} not in portfolio, you cannot delete', 'danger')
        return redirect(url_for('index'))

    user.currencies.remove(currency)
    db.session.commit()
    flash(f'{currency} successfully removed from your portfolio', 'info')

    return redirect(url_for('show_user_currencies'))


@app.route('/currency/market/<int:crypto_id>')
@login_required
def get_market_info(crypto_id):

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

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)["data"]
        filtered = [x for x in data if x["id"] == crypto_id]
        print(filtered)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    return render_template('details.html', data=filtered[0])



