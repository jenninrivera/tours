#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Doctor, Patient, Appointment

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.get("/")
def index():
    return "doctor/patient"

@app.get('/doctors')
def get_doctors():
    doctors = Doctor.query.all()
    data = [doctor.to_dict() for doctor in doctors]
    return make_response(jsonify(data), 200)

@app.get('/doctors/<int:id>')
def get_doctor_by_id(id):
    doctor = Doctor.query.filter(Doctor.id == id).first()
    if not doctor:
        make_response(jsonify({'error':'a quack'}), 404)
    doctor_dict = doctor.to_dict()
    # appointments = []
    # for a in doctor.appointments:
    #     appointment_dict = a.to_dict()
    #     appointment_dict['patient'] = a.patient_object.to_dict()
    #     appointments.append(appointment_dict)
    # doctor_dict['appointments'] = appointments
    return make_response(jsonify(doctor_dict), 200)

@app.post('/doctors')
def post_doctor():
    data = request.get_json()

    try:
        doc = Doctor(name=data['name'], specialty=data['specialty'])
        db.session.add(doc)
        db.session.commit()
        return make_response(jsonify(doc.to_dict()), 201)
    except ValueError:
        return make_response(jsonify({'error': "that's a quack!"}), 405)

@app.patch('/patients/<int:id>')
def patch_patients(id):
    data = request.get_json()
    patient = Patient.query.filter(Patient.id == id).first()

    try: 
        for key in data:
            setattr(patient, key, data[key])
        db.session.add(patient)
        db.session.commit()
        return make_response(jsonify(patient.to_dict()), 201)
    except ValueError:
        return make_response(jsonify({'error': "no such patient"}), 405)
        



if __name__ == "__main__":
    app.run(port=5555, debug=True)
