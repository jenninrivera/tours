from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from shared import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    blogs = db.relationship("Blog", back_populates="user")

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Blog(db.Model):
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    content = db.Column(db.String)
    title = db.Column(db.String)

    user = db.relationship("User", back_populates="blogs")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content,
            "title": self.title,
        }


"""
class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
"""
