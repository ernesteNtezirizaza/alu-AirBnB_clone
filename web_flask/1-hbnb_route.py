#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns the string "Hello HBNB!" to the client"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns the string "HBNB" to the client"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
