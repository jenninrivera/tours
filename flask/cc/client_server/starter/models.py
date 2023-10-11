from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Server(db.Model, SerializerMixin):
    __tablename__ = "server_table"
    serialize_rules = ("-messages.server",)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    messages = db.relationship("Message", back_populates="server")
    clients = association_proxy("messages", "client")

    @validates("name")
    def validates_name(self, key, name):
        if not (name.isupper() and name.isalpha()):
            raise ValueError("Name but be all in upper case.")
        return name

class Message(db.Model, SerializerMixin):
    __tablename__ = "message_table"
    serialize_rules = ("-server.messages", "-client.messages")
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey("server_table.id"), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client_table.id"), nullable=False)

    server = db.relationship("Server", back_populates="messages")
    client = db.relationship("Client", back_populates="messages")

    @validates("content")
    def validates_content(self, key, content):
        if content == "":
            raise ValueError("Content cannot be empty")
        return content
class Client(db.Model, SerializerMixin):
    __tablename__ = "client_table"
    serialize_rules = ("-messages.client",)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    messages = db.relationship("Message", back_populates="client")
    servers = association_proxy("messages", "server")
