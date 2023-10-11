#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Client, Server, Message  # import your models here!

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.get("/")
def index():
    return "client/server"

@app.get('/clients')
def get_clients():
    clients = Client.query.all()
    client_json_list =[]
    for client in clients:
        client_dict = client.to_dict(rules=("-messages",))
        server_dict_list = [s.to_dict(rules=("-messages",)) for s in client.servers]
        client_dict['servers'] = server_dict_list
        client_json_list.append(client_dict)
    return make_response(jsonify(client_json_list), 200)

@app.post('/messages')
def post_message():
    data = request.json
    try:
        new_message = Message(content=data.get("content"), server_id=data.get("server_id"), client_id=data.get('client_id'))
        db.session.add(new_message)
        db.session.commit()
        return make_response(jsonify(new_message.to_dict(rules=("-client_id", "-server_id",))), 201)
    except ValueError as e:
        print(e)
        return make_response(jsonify({"error":"message cannot be added"}), 404)
    
@app.post("/servers")
def post_server():
    data = request.json
    try:
        new_server = Server(name=data.get('name'))
        db.session.add(new_server)
        db.session.commit()
        return make_response(jsonify(new_server.to_dict(rules=("-messages",))), 200)
    except ValueError as e:
        print(e)
        return make_response(jsonify({"error":"bad request"}), 404)
    
@app.patch('/messages/<int:id>')
def patch_messages(id):
    data = request.json
    message = db.session.get(Message, id)
    if not message:
        return make_response(jsonify({"error":"message does not exist"}), 404)
    try:
        for key in data:
            setattr(message, key, data[key])
        db.session.add(message)
        db.session.commit()
        return make_response(jsonify(message.to_dict(rules=("-client", "-client_id", "-server", "-server_id",))), 201)
    except ValueError as e:
        print(e)
        return make_response(jsonify({"error":"bad request"}), 404)
    
@app.delete('/messages/<int:id>')
def delete_messages(id):
    message = Message.query.filter(Message.id == id).first()
    if not message:
            return make_response({"error": "message does not exist"}, 404)
    db.session.delete(message)
    db.session.commit()
    return make_response({}, 200)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
