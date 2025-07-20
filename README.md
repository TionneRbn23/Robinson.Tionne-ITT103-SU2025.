# Robinson.Tionne-ITT103-SU2025.
Author: Tionne Robinson
Date Created: Jul 19, 2025
Course: ITT103
Github Public URL: 


The purpose of the program
The idea behind this program is to allow the staff to do less work. I have created an automated program that gives patients an automated identification code that can be used to identify them in the system, book an appointment, cancel or reschedule. We also do the same for doctor’s, while also giving them a schedule and a fixed amount of booking for each day based on the doctor’s speciality. 
How to run it
The program begins with an introduction to the Healthcare clinic, and a display of the services that are offered. It then asks the users if they are a doctor or patient. This is done so medical professions know which area they expertise would be needed and patients know what is being offered at the hospital. Once the user enters if they are a patient/doctor, we ask if they have a patient ID or if they need one. If they need one, we request their name, age and gender. Once this information is accurately entered they are provided with a random patient id created by the program. Then we follow up by asking what services they would like to do, book, reschedule or cancel. If they would like to book an appointment for. If they enter  a service not provided, they will reach an error message requesting them to enter something that we do offer, however once one of the correct specialities is entered the program follows up by displaying the days the doctor would be available to see the patient, and allows them to see a time. Each doctor is allowed to see 5 patients on their available days, if two patients select the same day/time they are given an error message and asked to select another day/time. Once they have an available day, they are shown the additional services offered with this speciality and ask if they would require any and to enter them. When they enter this, their bill is displayed along with the name of the doctor, service they booked, the time along with the breakdown of the service they booked.
Required modifications:
I would suggest to make the program more efficient to add:
The option for doctors to enter their ID’s and be able to view their schedule for the week/day.
Allow patients to choose the doctor that they would like in the case where they may have a preference.
Instead of using their ID’s, patients would create a password as well to access their booking appointments for security purposes.
Allow patients to book more than one appointment or do more than one speciality.
Assumptions and limitations
There is no way for users to edit the information saved, so in the essence that there is incorrect information saved under their ID, we can’t change it.
The program doesn’t take a doctor's schedule in mind, in the event that a doctor can’t actually work. The appointment will still be booked as long as the slot is open.
It doesn’t actually have a big database where the information is saved forever. So we can’t go back and see a doctor’s previous appointment or a patient’s history.
When entering the day they would like to book the appointment for, The day is case sensitive, so if they enter the day without capitalization the program would give them an error message.
