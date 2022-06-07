import flask
import  datetime

from flask import render_template


app = flask.Flask(__name__)


@app.route('/<username>')
def index(username):
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    if time >= '08:00:00' and time  < '13:00:00':
        message = 'Good morning'
    elif time >= '13:00:00' and time < '17:00:00':
        message = 'Good afternoon'
    return render_template('./index.html', date=date, time=time, message=message, username=username)


if __name__ == '__main__':
    app.run(debug=True, port=4000)