from __future__ import absolute_import, unicode_literals
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"
