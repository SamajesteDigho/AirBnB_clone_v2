#!/usr/bin/python3
"""
    Here is the script for lauching the script
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(req):
    """ Tear down every thing """
    storage.close()


@app.route("/cities_by_states")
def cities_by_states():
    """ Home function """
    data1 = storage.all(cls=State)
    states = [x for _, x in data1.items()]
    
    for state in states:
        state.cities

    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    """ Run the app with parameters """
    app.run(host="0.0.0.0", port=5000)
