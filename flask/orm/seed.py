from faker import Faker
from models import User, Post
from random import choice
from shared import db, app

fake = Faker()


def create_users() -> list[User]:
    users = []
    for _ in range(10):
        users.append(User(name=fake.name()))
    return users


def create_posts(users: list[User]) -> list[Post]:
    posts = []
    for _ in range(10):
        random_user = choice(users)
        posts.append(Post(user_id=random_user.id, content=fake.text()))
    return posts


with app.app_context():
    User.query.delete()
    Post.query.delete()

    users = create_users()

    db.session.add_all(users)
    db.session.commit()
    posts = create_posts(users)

    db.session.add_all(posts)

    db.session.commit()
