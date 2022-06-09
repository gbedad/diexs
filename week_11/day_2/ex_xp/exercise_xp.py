import flask
from flask import render_template


app = flask.Flask(__name__)


@app.route('/')
def cv():
    html = render_template('./index.html')
    return html # redandant var


if __name__ == "__main__":
    app.run(port=3000)
