from flask import make_response, jsonify, request, g
from shared import app,db
from models import User, Post


@app.route("/")
def root():
    return "<h1>Simple blog site</h1>"


@app.get("/users")
def get_users():
    users = User.query.all()
    data = [user.to_dict() for user in users]
    return make_response(jsonify(data), 200)
@app.post('/users')
def post_user():
    user_data = request.get_json()
    user = User(name=user_data['name'])
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

@app.get("/users/<int:id>")
def get_user_by_id(id: int):
    user = User.query.filter(User.id == id).first()
    # import ipdb; ipdb.set_trace()
    print(user.posts)
    print(user.to_dict())
    return make_response(jsonify(user.to_dict()), 200)


@app.get("/users/<int:id>/posts")
def get_posts_for_user(id: int):
    user = User.query.filter(User.id == id).first()
    posts = [post.to_dict() for post in user.posts]

    return make_response(jsonify(posts),200)

@app.post('/users/<int:id>/posts')
def new_post_for_user(id:int):
    post_data = request.get_json()
    post = Post(user_id=id, content = post_data['content'])
    db.session.add(post)
    db.session.commit()
    
    return make_response(jsonify(post.to_dict()), 201)

@app.post('/users')
def new_user():
    return ''

if __name__ == "__main__":
    app.run(port=5555, debug=True)
