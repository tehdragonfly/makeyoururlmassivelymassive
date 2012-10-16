from __future__ import absolute_import, unicode_literals
from flask import abort, Flask, redirect, render_template, request
from hashlib import sha1
from makeyoururlmassivelymassive.db import session, MassiveURL
from sqlalchemy.exc import IntegrityError
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
    if "url" in request.form:
        url_id = sha1(request.form["url"]).hexdigest()
        try:
            session.add(MassiveURL(id=url_id, url=request.form["url"]))
            session.commit()
        except IntegrityError:
            # If it's the same hash, it's (probably) the same URL so we just
            # ignore it.
            pass
        for n in range(4):
            url_id += sha1(url_id).hexdigest()
        return url_id
    abort(400)

@app.route("/<id>")
def look_up(id):
    id = id[:40]
    try:
        url = session.query(MassiveURL).filter(MassiveURL.id==id).one()
        return redirect(url.url)
    except:
        abort(404)
