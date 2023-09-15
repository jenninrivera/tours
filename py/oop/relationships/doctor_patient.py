'''
Doctor
    name : str
    specialty : str

    Properties
        name must start with "Dr."
Appointment
    day : str
    patient : Patient
    doctor : Doctor
    
    Properties
        day must be M T W Th F
Patient
    name : str
    symptom : str

    Properties
        symptom must not be empty
'''

class Doctor:
    
    def __init__(self, name, specialty) -> None:
        self.name = name
        self.specialty = specialty
        self.appointments = []
        @property
        def name(self):
            return self._name
        @name.setter
        def name(self, name):
            if not name.startswith("Dr."):
                raise ValueError("hey that's a quack")
            self._name = name
class Appointment:
    def __init__(self, day, patient, doctor) -> None:
        self.day = day
        self.patient = patient
        self.doctor = doctor
        doctor.appointments.append(self)
        patient.appointments.append(self)
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if day not in ['M', 'T', 'W', 'Th', 'F']:
            raise ValueError("This doc don't work on weekends")
        self._day = day
class Patient:
    def __init__(self, name, symptom) -> None:
        self.name = name
        self.symptom = symptom
        self.appointments = []
        @property
        def symptom(self):
            return self._symptom
        @symptom.setter
        def symptom(self, symptom):
            if symptom== '':
                raise ValueError("this patient's fine!!")
            self._symptom = symptom

p1 = Patient('Roger Amsworth', 'melancolic')
d1 = Doctor('Dr. Baumgartner', 'Humour Imbalance')
a1 = Appointment('F', p1, d1)
