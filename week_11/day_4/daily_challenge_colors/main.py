import flask
from flask import render_template, url_for

app = flask.Flask(__name__)


@app.route('/blue')
def color_blue():
    return render_template('blue.html')


@app.route('/red')
def color_red():
    return render_template('red.html')


@app.route('/green')
def color_green():
    return render_template('green.html')


@app.route('/yellow')
def color_yellow():
    return render_template('yellow.html')


with app.test_request_context():
    print(url_for('color_blue'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)


