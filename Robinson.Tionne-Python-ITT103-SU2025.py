import random

def generate_patient_id():
    return f"P{random.randint(1000,9999)}"

def generate_doctor_id():
    return f"D{random.randint(1000,9999)}"

specialty_schedule = {
    'general': ['Monday', 'Thursday', 'Saturday'],
    'ophthalmologist': ['Tuesday', 'Thursday'],
    'gynaecologist': ['Tuesday', 'Friday'],
    'dentist': ['Wednesday', 'Thursday', 'Friday']
}

service_prices = {
    'general': 5000,
    'ophthalmologist': 4500,
    'gynaecologist': 4000,
    'dentist': 3500
}

additional_services = {
    'ophthalmologist': {
        'prescription': 500,
        'lens': 1500,
        'replacement': 1000
    },
    'gynaecologist': {
        'blood test': 1500,
        'pap smear': 2500,
        'mammogram': 2500
    },
    'dentist': {
        'whitening': 500,
        'cleaning': 1500,
        'wisdom tooth removal': 12000,
        'braces consultation': 5500
    }
}

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Patient(Person):
    def __init__(self, name, age, gender, patient_id):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.appointment_list = []

    def book_appointment(self, appointment):
        self.appointment_list.append(appointment)

    def view_profile(self):
        self.display()
        print(f"Patient ID: {self.patient_id}")

    def view_appointments(self):
        if not self.appointment_list:
            print("No appointments found.")
        for appt in self.appointment_list:
            print(f"Appointment ID: {appt.appointment_id}, Doctor: {appt.doctor.name}, Date: {appt.date}, Time: {appt.time}, Status: {appt.status}")

    def cancel_appointment(self, appointment_id):
        for appt in self.appointment_list:
            if appt.appointment_id == appointment_id:
                appt.cancel()
                print("Appointment cancelled.")
                return
        print("Appointment not found.")

    def reschedule_appointment(self, appointment_id, new_date, new_time):
        for appt in self.appointment_list:
            if appt.appointment_id == appointment_id and appt.status == 'Confirmed':
                available_doctors = [doc for doc in hs.get_doctor_by_specialty(appt.doctor.specialty) if doc.is_available(new_date)]
                if available_doctors:
                    new_doctor = available_doctors[0]
                    new_doctor.book_slot(new_date)
                    appt.doctor = new_doctor
                    appt.date = new_date
                    appt.time = new_time
                    print("Appointment rescheduled successfully.")
                    return
                else:
                    print("No available doctors on that day.")
                    return
        print("Appointment not found or already cancelled.")

class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialty):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialty = specialty
        self.schedule = {day: 5 for day in specialty_schedule[specialty]}

    def is_available(self, day):
        return self.schedule.get(day, 0) > 0

    def book_slot(self, day):
        if self.is_available(day):
            self.schedule[day] -= 1
            return True
        return False

    def view_schedule(self):
        print(f"Doctor {self.name} Schedule:")
        for day, slots in self.schedule.items():
            print(f"{day}: {slots} slots remaining")

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = 'Confirmed'

    def confirm(self):
        self.status = 'Confirmed'

    def cancel(self):
        self.status = 'Cancelled'

class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    def add_patient(self, name, age, gender):
        patient_id = generate_patient_id()
        patient = Patient(name, age, gender, patient_id)
        self.patients[patient_id] = patient
        print(f"Patient Registered. ID: {patient_id}")
        return patient

    def add_doctor(self, name, age, gender, specialty):
        doctor_id = generate_doctor_id()
        doctor = Doctor(name, age, gender, doctor_id, specialty)
        self.doctors[doctor_id] = doctor
        print(f"Doctor Registered. ID: {doctor_id}")
        return doctor

    def get_doctor_by_specialty(self, specialty):
        return [doc for doc in self.doctors.values() if doc.specialty == specialty]

    def book_appointment(self, patient_id, specialty, date, time):
        patient = self.patients.get(patient_id)
        if not patient:
            print("Patient not found. Let's register you first.")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            patient = self.add_patient(name, age, gender)
            patient_id = patient.patient_id

        doctors = self.get_doctor_by_specialty(specialty)
        for doctor in doctors:
            if doctor.is_available(date):
                doctor.book_slot(date)
                appointment_id = f"A{random.randint(1000,9999)}"
                appointment = Appointment(appointment_id, patient, doctor, date, time)
                self.appointments.append(appointment)
                patient.book_appointment(appointment)
                print(f"Appointment Booked with Dr. {doctor.name} on {date} at {time}. Appointment ID: {appointment_id}")
                return

        print("No available slots for selected date.")

    def generate_bill(self, specialty, selected_services):
        total = service_prices[specialty]
        print(f"The base Fee for {specialty.title()}: ${total}")
        if selected_services:
            for service in selected_services:
                cost = additional_services[specialty].get(service, 0)
                total += cost
                print(f"{service.title()}: ${cost}")
        print(f"Total Bill: ${total}")
        return total

# user interactive section
hs = HospitalSystem()

print("Welcome to the Welcome to Tionne Healthcare Clinic")
print("The services we offer are: General Check-up, Ophthalmologist, Gynaecologist, Dentist")

while True:
    user_type = input("Are you a patient or doctor? (patient/doctor/exit): ").lower()
    if user_type == 'exit':
        print("Thank you for visiting Tionne Healthcare Clinic. We hope to see you again.")
        break

    elif user_type == 'doctor':
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        specialty_input = input("Enter Specialty (general/ophthalmologist/gynaecologist/dentist): ").lower()
        if specialty_input in specialty_schedule:
            specialty = specialty_input
            hs.add_doctor(name, age, gender, specialty)
        else:
            print("Invalid specialty. Please restart and enter one of the listed specialties.")

    elif user_type == 'patient':
        patient_id = input("Enter your Patient ID (or press Enter to register): ")
        if not patient_id or patient_id not in hs.patients:
            print("Patient not found or new user. Registering now...")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            patient = hs.add_patient(name, age, gender)
            patient_id = patient.patient_id
        else:
            patient = hs.patients[patient_id]

        action = input("Would you like to book, view, cancel, or reschedule an appointment? (book/view/cancel/reschedule): ").lower()

        if action == 'book':
            specialty_input = input("Enter Specialty (general/ophthalmologist/gynaecologist/dentist): ").lower()
            if specialty_input in specialty_schedule:
                specialty = specialty_input
                print("Available Days:", ', '.join(specialty_schedule[specialty]))
                date_input = input("Please select your Appointment Day: ")
                if date_input in specialty_schedule[specialty]:
                    date = date_input
                    time = input("Please enter Time (e.g., 10:00AM): ")
                    hs.book_appointment(patient_id, specialty, date, time)

                    if specialty in additional_services:
                        print("Available Additional Services:")
                        for service, price in additional_services[specialty].items():
                            print(f"{service.title()} - ${price}")
                        selected_services = input("Enter any additional services separated by commas (or leave blank): ").lower().split(',')
                        selected_services = [s.strip() for s in selected_services if s.strip() in additional_services[specialty]]
                    else:
                        selected_services = []

                    hs.generate_bill(specialty, selected_services)
                else:
                    print("Doctor not available on this day. Please choose a valid day.")
            else:
                print("Invalid specialty. Please choose from the available options.")

        elif action == 'view':
            patient.view_appointments()

        elif action == 'cancel':
            appt_id = input("Enter Appointment ID to cancel: ")
            patient.cancel_appointment(appt_id)

        elif action == 'reschedule':
            appt_id = input("Enter Appointment ID to reschedule: ")
            new_date = input("Enter new appointment day: ")
            new_time = input("Enter new time (e.g., 2:00PM): ")
            patient.reschedule_appointment(appt_id, new_date, new_time)

        else:
            print("Invalid action. Please choose book, view, cancel, or reschedule.")
    else:
        print("Invalid option.")