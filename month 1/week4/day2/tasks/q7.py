class Patient:
    def __init__(self, blood_group):
        valid_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        if blood_group not in valid_groups:
            raise ValueError("Invalid blood group")

        self.__blood_group = blood_group

    def get_blood_group(self):
        return self.__blood_group

    def set_blood_group(self, blood_group):
        valid_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        if blood_group not in valid_groups:
            raise ValueError("Invalid blood group")

        self.__blood_group = blood_group


# Example
p = Patient("A+")
print(p.get_blood_group())

p.set_blood_group("O-")
print(p.get_blood_group())