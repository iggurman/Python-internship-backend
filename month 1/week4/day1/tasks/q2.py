class Student:
    def __init__(self, student_id, name, age, gender, class_name, section, roll_number, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.class_name = class_name
        self.section = section
        self.roll_number = roll_number
        self.marks = marks

    def study(self):
        return f"{self.name} is studying in {self.class_name}."

    def attend_class(self):
        return f"{self.name} is attending the class."

    def take_exam(self):
        return f"{self.name} is taking the exam."

    def show_result(self):
        if self.marks >= 35:
            result = "Passed"
        else:
            result = "Failed"

        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Class: {self.class_name}\n"
            f"Section: {self.section}\n"
            f"Roll Number: {self.roll_number}\n"
            f"Marks: {self.marks}\n"
            f"Result: {result}"
        )

    def show_profile(self):
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Class: {self.class_name}\n"
            f"Section: {self.section}\n"
            f"Roll Number: {self.roll_number}\n"
            f"Marks: {self.marks}"
        )


s1 = Student(1, "Gurman", 22, "Male", "MCA", "A", 101, 89)

print(s1.study())
print(s1.attend_class())
print(s1.take_exam())
print()
print(s1.show_result())
print()
print(s1.show_profile())