import flask
from flask import render_template, url_for

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/<string:page_color>') # as we menthened at the class string by default its string
def color(page_color):
    return render_template(page_color)

#
# with app.test_request_context():
#     print(url_for(color))


if __name__ == '__main__':
    app.run(port=3000, debug=True)


