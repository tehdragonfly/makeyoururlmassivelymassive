from __future__ import absolute_import, unicode_literals
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello World!"

@app.route("/", methods=["POST"])
def create():
    return "Hello World!"

@app.route("/<url>")
def look_up(url):
    return "Hello World!"
