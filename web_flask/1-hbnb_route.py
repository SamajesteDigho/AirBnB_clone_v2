#!/usr/bin/python3
"""
    Here is the initialization script
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """ Here is the index function """
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """ Here the hbnb function """
    return "HBNB"
