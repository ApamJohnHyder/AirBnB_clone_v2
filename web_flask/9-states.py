#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


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


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_html(id=None):
    """ Function called with /states route """
    states = storage.all(State)

    if not id:
        dict_to_html = {value.id: value.name for value in states.values()}
        return render_template('7-states_list.html',
                               Table="States",
                               items=dict_to_html)

    k = "State.{}".format(id)
    if k in states:
        return render_template('9-states.html',
                               Table="State: {}".format(states[k].name),
                               items=states[k])

    return render_template('9-states.html',
                           items=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> fa35fa4d506a850808a3e11a3c43c384b95f2deb
