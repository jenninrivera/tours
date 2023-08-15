from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from shared import db


class User(db.Model):
    __tablename__ = "user"

    serialize_rules = "-post.user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    posts = db.relationship("Post", back_populates="user")

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    content = db.Column(db.String)

    user = db.relationship("User", back_populates="posts")

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "content": self.content}
