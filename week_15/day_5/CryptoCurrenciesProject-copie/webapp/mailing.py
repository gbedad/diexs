from flask import url_for, render_template
from flask_mail import Message
from webapp import mail


def send_email(user):
    msg = Message(f'Information Request',
                  sender='noreply@gmail.com',
                  recipients=[user.email])
    msg.body = f'''Test message
    '''
    mail.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('Password reset',
               sender="mymail@gmail.com",
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user, token=token),
               html_body=render_template('email/reset_password.html', user=user, token=token))
