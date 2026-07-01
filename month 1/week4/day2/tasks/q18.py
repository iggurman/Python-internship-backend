class Hospital:
    def __init__(self, doctor, room):
        self.__doctor_name = doctor
        self.__room_number = room

    def admit(self, doctor, room):
        self.__doctor_name = doctor
        self.__room_number = room

    def discharge(self):
        self.__doctor_name = None
        self.__room_number = None
        print("Patient Discharged")

    def get_details(self):
        return self.__doctor_name, self.__room_number


h = Hospital("Dr. Sharma", 101)

print(h.get_details())

h.discharge()

print(h.get_details())