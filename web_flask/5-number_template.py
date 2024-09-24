#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns the string "Hello HBNB!" to the client"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns the string "HBNB" to the client"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def echo(text):
    """Returns the string "C" followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Returns the string "Python" followed by the value of the text arg"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns the string "n is a number" only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns an HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
