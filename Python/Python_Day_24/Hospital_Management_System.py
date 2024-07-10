class Patient:

    def __init__(self, patient_id, name, medical_history=None):
        self.patient_id = patient_id
        self.name = name
        self.medical_history = medical_history if medical_history is not None else []

    def __str__(self):
        return f"Patient(ID: {self.patient_id}, Name: {self.name})"
    
class Doctor:
    doctors = []

    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        Doctor.doctors.append(self)

    def __str__(self):
        return f"Doctor(ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty})"
    
class Appointment:
    appointments = []

    def __init__(self, date, time, patient, doctor):
        self.date = date
        self.time = time
        self.patient = patient
        self.doctor = doctor
        self.status = 'Scheduled'
        Appointment.appointments.append(self)

    def reschedule(self, new_date, new_time):
        self.date = new_date
        self.time = new_time
        self.status = 'Rescheduled'

    def cancel(self):
        self.status = 'Canceled'
        Appointment.appointments.remove(self)

    def __str__(self):
        return (f"Appointment(Date: {self.date}, Time: {self.time}, "
                f"Patient: {self.patient.name}, Doctor: {self.doctor.name}, Status: {self.status})")
    
if __name__ == "__main__":
    # Create patients
    patient1 = Patient(1, "John Doe")
    patient2 = Patient(2, "Jane Smith", ["Diabetes"])

    # Create doctors
    doctor1 = Doctor(1, "Dr. Alice", "Cardiology")
    doctor2 = Doctor(2, "Dr. Bob", "Neurology")

    # Schedule appointments
    appointment1 = Appointment("2024-07-10", "10:00", patient1, doctor1)
    appointment2 = Appointment("2024-07-11", "11:00", patient2, doctor2)

    # Print appointments
    print("Scheduled Appointments:")
    for appt in Appointment.appointments:
        print(appt)

    # Reschedule an appointment
    appointment1.reschedule("2024-07-12", "09:00")
    print("\nAfter Rescheduling Appointment 1:")
    for appt in Appointment.appointments:
        print(appt)

    # Cancel an appointment
    appointment2.cancel()
    print("\nAfter Canceling Appointment 2:")
    for appt in Appointment.appointments:
        print(appt)

        
        
        