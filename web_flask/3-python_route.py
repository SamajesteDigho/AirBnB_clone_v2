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


@app.route("/c/<text>")
def cfun(text):
    """ Here the c_is_fun function """
    string = text
    string = string.replace('_', ' ')
    return "C {}".format(string)


@app.route("/python")
@app.route("/python/<text>")
def python(text="is_cool"):
    """ Here the python function """
    string = text
    string = string.replace('_', ' ')
    return "Python {}".format(string)


if __name__ == "__main__":
    """ Here the initializer """
    app.run(host="0.0.0.0", port=5000)
