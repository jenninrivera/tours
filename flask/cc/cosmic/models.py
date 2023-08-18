from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class Planet(db.Model, SerializerMixin):
    __tablename__ = "planet"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    distance_from_earth = db.Column(db.Integer)
    nearest_star = db.Column(db.String)

    # Add relationship

    missions = db.relationship("Mission", cascade="all, delete-orphan", back_populates="planet")

    # Add serialization rules
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "distance_from_earth": self.distance_from_earth,
            "nearest_star": self.nearest_star,
        }


class Scientist(db.Model, SerializerMixin):
    __tablename__ = "scientist"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    field_of_study = db.Column(db.String)

    # Add relationship
    missions = db.relationship("Mission", cascade="all, delete-orphan",  back_populates="scientist")

    # Add serialization rules
    def to_dict(self):
        return {"id": self.id, "name": self.name, "field_of_study": self.field_of_study}

    # Add validation
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError()
        return name

    @validates("field_of_study")
    def validate_fos(self, key, fos):
        if not fos:
            raise ValueError()
        return fos


class Mission(db.Model, SerializerMixin):
    __tablename__ = "mission"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    scientist_id = db.Column(db.Integer, db.ForeignKey("scientist.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))

    # Add relationships
    planet = db.relationship("Planet", back_populates="missions")
    scientist = db.relationship("Scientist", back_populates="missions")

    # Add serialization rules
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "scientist_id": self.scientist_id,
            "planet_id": self.planet_id,
        }

    # Add validation
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError()
        return name

    @validates("scientist_id")
    def validate_sid(self, key, sid):
        if not sid:
            raise ValueError("Mission has no scientist")
        return sid

    @validates("planet_id")
    def validate_pid(self, key, pid):
        if not pid:
            raise ValueError("Mission has no planet")
        return pid

