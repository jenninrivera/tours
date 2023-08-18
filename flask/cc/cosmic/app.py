#!/usr/bin/env python3

from models import db, Scientist, Mission, Planet
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return ""


@app.get("/scientists")
def get_scientists():
    scientists = Scientist.query.all()
    data = [s.to_dict() for s in scientists]
    print(data)
    return make_response(jsonify(data), 200)


@app.get("/scientists/<int:id>")
def get_scientist_by_id(id: int):
    s = Scientist.query.filter(Scientist.id == id).first()
    if not s:
        return make_response(jsonify({"error": "Scientist not found"}), 404)
    import ipdb; ipdb.set_trace()
    missions: list[dict] = []
    for m in s.missions:
        m_dict = m.to_dict()
        m_dict["planet"] = m.planet.to_dict()
        missions.append(m_dict)
    s_dict = s.to_dict()
    s_dict["missions"] = missions
    return make_response(jsonify(s_dict), 200)


@app.get("/planets")
def get_planets():
    planets = Planet.query.all()
    data = [p.to_dict() for p in planets]
    return make_response(jsonify(data), 200)


@app.post("/missions")
def post_missions():
    request_data = request.get_json()
    try:
        m = Mission(
            name=request_data["name"],
            scientist_id=request_data["scientist_id"],
            planet_id=request_data["planet_id"],
        )
        db.session.add(m)
        db.session.commit()
        m_dict = m.to_dict()
        m_dict["planet"] = m.planet.to_dict()
        m_dict["scientist"] = m.scientist.to_dict()
        return make_response(jsonify(m_dict), 201)
    except ValueError:
        return make_response(jsonify({'errors':['validation errors']}), 400)


@app.post("/scientists")
def post_scientists():
    request_data = request.get_json()
    try:
        s = Scientist(
            name=request_data["name"], field_of_study=request_data["field_of_study"]
        )
        db.session.add(s)
        db.session.commit()
        return make_response(jsonify(s.to_dict()), 201)
    except ValueError:
        return make_response(jsonify({'errors':['validation errors']}), 400)


@app.patch("/scientists/<int:id>")
def patch_scientist(id: int):
    s = Scientist.query.filter(Scientist.id == id).first()
    if not s:
        return make_response(jsonify({"error": "Scientist not found"}), 404)
    request_data = request.get_json()
    try:
        for key in request_data:
            setattr(s, key, request_data[key])
        db.session.add(s)
        db.session.commit()
        return make_response(jsonify(s.to_dict()), 202)
    except ValueError:
        return make_response(jsonify({'errors':['validation errors']}), 400)


@app.delete("/scientists/<int:id>")
def delete_scientist(id: int):
    s = Scientist.query.filter(Scientist.id == id).first()
    if not s:
        return make_response(jsonify({"error": "Scientist not found"}), 404)
    db.session.delete(s)
    db.session.commit()
    return make_response(jsonify({}), 204)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
