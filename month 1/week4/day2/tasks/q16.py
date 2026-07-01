class School:
    def __init__(self, strength):
        self.__student_strength = strength

    def add_student(self):
        self.__student_strength += 1

    def remove_student(self):
        if self.__student_strength > 0:
            self.__student_strength -= 1

    def get_strength(self):
        return self.__student_strength


s = School(50)

print(s.get_strength())

s.add_student()
print(s.get_strength())

s.remove_student()
print(s.get_strength())