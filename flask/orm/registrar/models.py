from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from shared import db, metadata


class Student(db.Model, SerializerMixin):
    __tablename__ = "student"
    serialize_rules = ("-enrollment.student",)
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    grad_year = db.Column(db.Integer)

    enrollments = db.relationship("Enrollment", back_populates="student")


class Enrollment(db.Model, SerializerMixin):
    __tablename__ = "enrollment"

    serialize_rules= ('-student.enrollments', '-course.enrollments')
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    term = db.Column(db.String)

    student = db.relationship("Student", back_populates="enrollments")
    course = db.relationship("Course", back_populates="enrollments")
    


class Course(db.Model, SerializerMixin):
    __tablename__ = "course"

    serialize_rules = ("-enrollment.course",)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    instructor = db.Column(db.String)
    credits = db.Column(db.Integer)

    enrollments = db.relationship("Enrollment", back_populates="course")
