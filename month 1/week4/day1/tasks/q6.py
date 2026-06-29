class Patient:
    def __init__(self, patient_id, name, age, gender,
                disease, doctor_name, room_number, blood_group):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.doctor_name = doctor_name
        self.room_number = room_number
        self.blood_group = blood_group

    def checkup(self):
        return f"{self.name} is undergoing a medical checkup."

    def admit(self):
        return f"{self.name} has been admitted to Room {self.room_number}."

    def discharge(self):
        return f"{self.name} has been discharged from the hospital."

    def take_medicine(self, medicine):
        return f"{self.name} is taking {medicine}."

    def show_report(self):
        return (
            f"Patient ID   : {self.patient_id}\n"
            f"Name         : {self.name}\n"
            f"Age          : {self.age}\n"
            f"Gender       : {self.gender}\n"
            f"Disease      : {self.disease}\n"
            f"Doctor       : {self.doctor_name}\n"
            f"Room Number  : {self.room_number}\n"
            f"Blood Group  : {self.blood_group}"
        )


p1 = Patient(101, "Gurman", 22, "Male",
            "Fever", "Dr. Sharma", 201, "B+")

p2 = Patient(102, "Avantika", 23, "Female",
            "Malaria", "Dr. Verma", 305, "A+")

p3 = Patient(103, "Ritik", 24, "Male",
            "Typhoid", "Dr. Mehta", 402, "O+")

p4 = Patient(104, "Soham", 21, "Male",
            "Dengue", "Dr. Gupta", 108, "AB+")

p5 = Patient(105, "Jaado", 25, "Male",
            "Cold", "Dr. Singh", 115, "B-")


print(p1.checkup())
print(p2.admit())
print(p3.take_medicine("Paracetamol"))
print(p4.discharge())
print()
print(p5.show_report()