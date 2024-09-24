#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns an HTML page with a list of all States in the database"""
    states = list(storage.all(State).values())
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
