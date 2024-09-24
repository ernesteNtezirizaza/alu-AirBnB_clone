#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def all_states():
    """Displays a page with all states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def one_state(id):
    """Displays a page with all citys of a state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='one')
    return render_template('9-states.html', states=state, mode='none')


@app.teardown_appcontext
def close_session(exception):
    """Closes the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
