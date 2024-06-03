#!/usr/bin/python3
"""
    The initialization script
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ Here the slash path. """
    return "Hello HBNB!"
