#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime
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
    data = [doctor.to_dict(rules=("-appointments",)) for doctor in doctors]
    
    return make_response(jsonify(data), 200)

@app.get('/doctors/<int:id>')
def doctor_by_id(id):
    doctor = Doctor.query.filter(Doctor.id == id).first()
    if not doctor:
        return make_response(jsonify({"error":"doctor does not exist"}), 404)
    return make_response(jsonify(doctor.to_dict(rules=("-appointments.patient_id", "-appointments.doctor_id"))), 200)

@app.get('/patients/<int:id>')
def patient_by_id(id):
    patient = Patient.query.filter(Patient.id == id).first()
    if not patient:
        return make_response(jsonify({"error":"patient does not"}), 404)
    doctors_dict_list = [d.to_dict(rules=("-appointments",)) for d in patient.doctors]
    patient_dict = patient.to_dict(rules=("-appointments",))
    patient_dict['doctors'] = doctors_dict_list
    return make_response(jsonify(patient_dict), 200)

@app.post('/doctors')
def post_doctor():
    data = request.json
    try:
        new_doctor = Doctor(name=data.get('name'), specialty=data.get('specialty'))
        db.session.add(new_doctor)
        db.session.commit()
        return make_response(jsonify(new_doctor.to_dict(rules=("-appointments",))), 201)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error":"bad doctor post"}), 404)


@app.post('/appointments')
def post_appointments():
    data = request.json
    try:
        new_appiontment = Appointment(day=data.get('day'), doctor_id=data.get('doctor_id'), patient_id=data.get('patient_id'))
        db.session.add(new_appiontment)
        db.session.commit()
        return make_response(jsonify(new_appiontment.to_dict(rules=('-doctor_id', '-patient_id',))), 201)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error":"invalid appiontment"}), 404)

@app.delete('/appointments/<int:id>')
def delete_appointment(id):
    appointment = Appointment.query.filter(Appointment.id == id).first()
    if not appointment:
            return make_response({"error":"appointment does not exist"}, 404)
    db.session.delete(appointment)
    db.session.commit()
    return make_response(jsonify({}), 200)

@app.patch('/patients/<int:id>')
def patch_patient(id):
    patient = Patient.query.filter(Patient.id == id).first()
    if not patient:
        return make_response({"error":"patient does not exist"}, 404)
    data = request.json
    try:
        for key in data:
            setattr(patient, key, data[key])
        db.session.add(patient)
        db.session.commit()
        return make_response(jsonify(patient.to_dict(rules=("-appointments",))), 201)
    except ValueError as e:
        print(e)
        return make_response(jsonify({"error":"bad request"}), 404)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
