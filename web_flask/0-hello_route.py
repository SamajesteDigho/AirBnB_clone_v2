#!/usr/bin/python3
"""
    The initialization script
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello HBNB!"
