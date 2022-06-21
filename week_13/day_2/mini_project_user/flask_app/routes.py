from flask import render_template, redirect, url_for
from flask_app import robots_app, db
from flask_app.models import User
from flask_app.forms import AddUser, Login


@robots_app.route('/')
def show_users():
    users = [user for user in User.query.all()]
    specific_user = User.query.filter_by(city='Roscoeview').first()
    first_5 = User.query.limit(5).all()
    start_with_5 = User.query.filter(User.zipcode.startswith('5')).all()
    return render_template('index.html', users=users, specific_user=specific_user,
                           start_with_5=start_with_5, first_5=first_5)


@robots_app.route('/login', methods=("GET", "POST"))
def login():
    login_form = Login()
    if login_form.validate_on_submit():
        name = login_form.name.data
        city = login_form.city.data
        print(name, city)
        user = User.query.filter((User.name == name) & (User.city == city)).first()
        print(user)
        if user is not None:
            return redirect('/')
        else:
            return redirect('/add_user')
    return render_template('login.html', form=login_form)


@robots_app.route('/add_user', methods=("GET", "POST"))
def add_user():
    add_user_form = AddUser()
    if add_user_form.validate_on_submit():  # Check if the form has been filled

        name = add_user_form.user_name.data  # Get
        street = add_user_form.street.data  # The
        city = add_user_form.city.data  # Data
        zipcode = add_user_form.zipcode.data  # Data

        print("Here is what I got from the form:")
        print("username:", name)
        print("street:", street)
        print("city:", city)
        print("zipcode:", zipcode)
        # Do something with the data
        model = User(name=name, street=street, city=city, zipcode=zipcode)
        db.session.add(model)
        db.session.commit()

        return redirect('/')
    return render_template('add_user.html', form=add_user_form)



