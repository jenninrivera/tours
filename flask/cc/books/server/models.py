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

    book_list = db.relationship(
        "Book", back_populates="author_object", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {"id": self.id, "name": self.name, "pen_name": self.pen_name}


class Book(db.Model, SerializerMixin):
    __tablename__ = "book_table"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    page_count = db.Column(db.Integer)

    author_id = db.Column(db.Integer, db.ForeignKey("author_table.id"))
    publisher_id = db.Column(db.Integer, db.ForeignKey("publisher_table.id"))

    author_object = db.relationship("Author", back_populates="book_list")
    publisher_object = db.relationship("Publisher", back_populates="book_list")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "page_count": self.page_count,
            "author_name": self.author_object.name,
            "publisher_name": self.publisher_object.name,
        }

    @validates("page_count")
    def validate_pc(self, key, pc):
        if pc < 1:
            raise ValueError("invalid page count")
        return pc


class Publisher(db.Model, SerializerMixin):
    __tablename__ = "publisher_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    founding_year = db.Column(db.Integer, nullable=False)

    book_list = db.relationship(
        "Book", back_populates="publisher_object", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {"id": self.id, "name": self.name, "founding_year": self.founding_year}

    @validates("founding_year")
    def validate_fy(self, key, fy):
        if fy < 1600 or fy > 2023:
            raise ValueError("invalid founding year")
        return fy
