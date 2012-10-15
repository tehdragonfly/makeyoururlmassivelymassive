from __future__ import absolute_import, unicode_literals
from flask import Flask, render_template
from makeyoururlmassivelymassive.db import session, MassiveURL
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

@app.teardown_request
def shutdown_session(exception=None):
    session.remove()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def create():
    return "Hello World!"

@app.route("/<id>")
def look_up(id):
    id = id[:32]
    url = session.query(MassiveURL).filter(MassiveURL.id==id).one()
    return redirect(url.url)
