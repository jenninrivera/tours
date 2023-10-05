from flask import make_response, jsonify, request, g
from flask import Flask
from models import db, Student, Course, Enrollment

from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def root():
    return "<h1>Registrar</h1>"


@app.get('/students')
def get_students():
    student_list = Student.query.all()
    student_json = []
    for student in student_list:
        student_json.append(student.to_dict(rules=("-enrollment_list",)))
    return make_response(jsonify(student_json), 200)

@app.get('/students/<int:id>')
def get_student_by_id(id):
    student = Student.query.filter(Student.id == id).first()
    if not student:
        return make_response(jsonify({"error":"no such student"}), 404)
    return make_response(jsonify(student.to_dict()), 200)

@app.get('/students/<int:id>/courses')
def get_course_for_student(id):
    student = Student.query.filter(Student.id == id).first()
    if not student:
        return make_response(jsonify({"error":"no such student"}), 404)
    courses = [course.to_dict(rules=("-enrollment_list",)) for course in student.courses]
    return make_response(jsonify(courses), 200)

@app.post('/students')
def post_student():
    request_data = request.json
    new_student = Student(fname = request_data['fname'], lname = request_data['lname'], grad_year = request_data['grad_year'])
    db.session.add(new_student)
    db.session.commit()
    return make_response(jsonify(new_student.to_dict()), 201)

@app.post('/students/<int:id>/enrollments')
def post_enrollment(id):
    student = db.session.get(Student, id)
    if not student:
        return make_response(jsonify({"error": "no such student"}))
    data = request.json
    try:
        enrollment = Enrollment(student_id=student.id, course_id=data['course_id'], term=data.get('term'))
        db.session.add(enrollment)
        db.session.commit()
    except ValueError as e:
        return make_response(jsonify({"error": "bad term"}))
    return make_response(jsonify(enrollment.to_dict(rules=("-student_object",)), 201))

    # my solution
    # request_data = request.json
    # new_student_enrollments = Enrollment(student_id = request_data['student_id'], course_id = request_data['course_id'], term = request_data['term'])
    # db.session.add(new_student_enrollments)
    # db.session.commit()
    # return make_response(jsonify(new_student_enrollments.to_dict()), 201)

@app.patch('/students/<int:id>')
def update_student(id):
    student = db.session.get(Student, id)
    if not student:
        return make_response(jsonify({"error": "no such student"}), 404)
    data = request.json
    try:
        for key in data:
            setattr(student, key, data[key])
        db.session.add(student)
        db.session.commit()
        return make_response(jsonify(student.to_dict(rules=("-enrollment_list",))), 201)
    except ValueError as e:
        print(e)
        return make_response(jsonify({"error": "bad grad year"}), 404)

@app.delete('/students/<int:id>')
def delete_student(id):
    student = Student.query.filter(Student.id == id).first()
    db.session.delete(student)
    db.session.commit()
    return make_response(jsonify({}), 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
