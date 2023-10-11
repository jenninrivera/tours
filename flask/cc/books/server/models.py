from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Author(db.Model, SerializerMixin):
    __tablename__ = "author_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    pen_name = db.Column(db.String)




class Book(db.Model, SerializerMixin):
    __tablename__ = "book_table"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    page_count = db.Column(db.Integer)



    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "page_count": self.page_count,
            "author_name": self.author_object.name,
            "publisher_name": self.publisher_object.name,
        }


class Publisher(db.Model, SerializerMixin):
    __tablename__ = "publisher_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    founding_year = db.Column(db.Integer, nullable=False)

