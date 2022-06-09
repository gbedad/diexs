from flask import Flask, render_template, url_for
from flaskext.markdown import Markdown


app = Flask(__name__)
Markdown(app)


@app.route('/lesson1')
def func_chapter():
    with open('./lesson1/in-this-chapter.md', 'r') as f:
        mkd_text = f.read()

    html = render_template("./index.html", mkd_text=mkd_text) # the var is redandant
    return html


@app.route('/exercises')
def func_exercises():
    with open('./lesson1/exercises.md', 'r') as f:
        mkd_text = f.read()

    html = render_template("./index.html", mkd_text=mkd_text)
    return html # the same the var is redundant


if __name__ == "__main__":
    app.run(port=8080, debug=True)
