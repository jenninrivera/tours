#!/usr/bin/env python3

from app import app
from models import db  # models go here
from faker import Faker
from random import randint, choice
from models import Author, Book, Publisher

fake = Faker()

if __name__ == "__main__":
    with app.app_context():
        print("Seeding database...")

        authors = []
        for _ in range(10):
            authors.append(Author(name=fake.name(), pen_name=fake.name()))
        db.session.add_all(authors)
        db.session.commit()

        publishers = []
        for _ in range(10):
            publishers.append(
                Publisher(
                    name=fake.name() + " Publishing House",
                    founding_year=randint(1600, 2023),
                )
            )
        db.session.add_all(publishers)
        db.session.commit()

        books = []
        for _ in range(10):
            books.append(
                Book(
                    title=fake.text().split()[0],
                    page_count=randint(98, 475),
                    author_id=choice(authors).id,
                    publisher_id=choice(publishers).id,
                )
            )
        db.session.add_all(books)
        db.session.commit()

        print("Seeding complete!")
