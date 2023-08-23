from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)

class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patient_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)

    # -list.object 
    serialize_rules = ('-appointments.patient_object', )
    appointments = db.relationship("Appointment", back_populates='patient_object', cascade='all, delete-orphan')
    # def to_dict(self):
    #     return {'id':self.id, 'name':self.name }
class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointment_table'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    #-object1.list -object2.list
    serialize_rules = ("-patient_object.appointments", "-doctor_object.appointments")

    patient_id = db.Column(db.Integer, db.ForeignKey("patient_table.id"))    
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor_table.id")) 

    patient_object = db.relationship("Patient", back_populates='appointments') 
    doctor_object = db.relationship("Doctor", back_populates='appointments') 

    # def to_dict(self):
    #     return {'id':self.id, 'patient_id':self.patient_id, 'doctor_id': self.doctor_id, 'date': self.date.strftime("%B %d, %Y")}

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctor_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    specialty = db.Column(db.String, nullable = False) 

    appointments = db.relationship("Appointment", back_populates='doctor_object', cascade='all, delete-orphan')
    serialize_rules = ('-appointments.doctor_object',)
    # def to_dict(self):
    #     return {'id':self.id, 'name':self.name, 'specialty': self.specialty}