#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.

    States/cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
""" runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_html():
    """ Function called with /states_list route """
    states = storage.all(State)
    return render_template('8-cities_by_states.html',
                           Table="States",
                           states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> fa35fa4d506a850808a3e11a3c43c384b95f2deb
