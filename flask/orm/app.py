from flask import make_response, jsonify, request, g
from shared import app
from models import User, Post


@app.route("/")
def root():
    return "<h1>Simple blog site</h1>"


@app.get("/users")
def get_users():
    return "test"


@app.get("/users/<int:id>")
def get_user_by_id(id: int):
    user = User.query.filter(User.id == id).first()
    # import ipdb; ipdb.set_trace()
    print(user.to_dict())
    return make_response(jsonify(user.to_dict()), 200)


@app.get("/users/<int:id>/posts")
def get_posts_for_user(id: int):
    return "test"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
