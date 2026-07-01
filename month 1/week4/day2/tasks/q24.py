class UniversityStudent:
    def __init__(self, cgpa):
        if cgpa < 0.0 or cgpa > 10.0:
            raise ValueError("CGPA should be between 0.0 and 10.0")
        self.__cgpa = cgpa

    @property
    def cgpa(self):
        return self.__cgpa

    @cgpa.setter
    def cgpa(self, value):
        if value < 0.0 or value > 10.0:
            raise ValueError("CGPA should be between 0.0 and 10.0")
        self.__cgpa = value


s = UniversityStudent(8.5)

print(s.cgpa)

s.cgpa = 9.2
print(s.cgpa)

