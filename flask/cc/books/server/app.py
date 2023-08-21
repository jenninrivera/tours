#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Book, Author, Publisher  # import your models here!

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.get("/")
def index():
    return "Hello world"


@app.get("/publishers/<int:id>")
def get_publisher_by_id(id: int):
    pub = Publisher.query.filter(Publisher.id == id).first()
    authors: list[dict] = []
    for book in pub.book_list:
        authors.append(book.author_object.to_dict())
    pub_dict = pub.to_dict()
    pub_dict["authors"] = authors

    return make_response(jsonify(pub_dict), 200)


@app.get("/books")
def get_books():
    books = Book.query.all()
    data = [b.to_dict() for b in books]
    return make_response(jsonify(data), 200)


# write your routes here!


@app.post("/books")
def post_book():
    request_data = request.get_json()
    try:
        book = Book(
            title=request_data["title"],
            page_count=request_data["page_count"],
            author_id=request_data["author_id"],
            publisher_id=request_data["publisher_id"],
        )
        db.session.add(book)
        db.session.commit()
        return make_response(jsonify(book.to_dict()), 202)
    except:
        return make_response(jsonify({"error": "ya messed up son"}), 405)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
