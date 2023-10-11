#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Right, Left, Middle  # import your models here!

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.get("/")
def index():
    return "right/left"

@app.get("/rights")
def get_rights():
    rights = Right.query.all()
    data = [right.to_dict(rules=("-middles",)) for right in rights]
    return make_response(jsonify(data), 200)

@app.get("/rights/<int:id>")
def get_right_by_id(id):
    right = Right.query.filter(Right.id == id).first()
    if not right:
        return make_response(jsonify({"error":"right does not exist"}))
    return make_response(jsonify(right.to_dict()), 200)

@app.post("/lefts")
def post_left():
    data = request.json
    try:
        new_left = Left(column=data.get("column"))
        db.session.add(new_left)
        db.session.commit()
        return make_response(jsonify(new_left.to_dict()), 200)
    except:
        return make_response(jsonify({"error":"cannot add left"}), 404)

@app.patch("/middles/<int:id>")
def patch_middle(id):
    middle_patch = db.session.get(Middle, id)
    if not middle_patch:
        return make_response(jsonify({"error":"middle does not exist"}), 404)
    data = request.json
    try:
        for key in data:
            setattr(middle_patch, key, data[key])
            db.session.add(middle_patch)
            db.session.commit()
            return make_response(jsonify(middle_patch.to_dict(rules=("-left", "-right",))), 200)
    except:
        return make_response(jsonify({"error":"could not update middle"}), 404)

@app.delete("/lefts/<int:id>")
def delete_left(id):
    left = Left.query.filter(Left.id == id).first()
    if not left:
        return make_response(jsonify({"eeror":"Left does not exist"}), 404)
    db.session.delete(left)
    db.session.commit()
    return make_response(jsonify({}), 200)
if __name__ == "__main__":
    app.run(port=5555, debug=True)
