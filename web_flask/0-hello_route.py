#!/usr/bin/python3
"""
    The initialization script
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False
if __name__ == "__main__":
    """ Here the initializer """
    app.run(host="0.0.0.0", port=5000)


@app.route("/")
def home():
    """ Here the slash path. """
    return "Hello HBNB!"
