class Employee:
    def __init__(self, employee_id, name, department, designation,salary, email, joining_date, experience):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary
        self.email = email
        self.joining_date = joining_date
        self.experience = experience

    def login(self):
        return f"{self.name} has logged in successfully."

    def apply_leave(self, days):
        return f"{self.name} has applied for {days} day(s) leave."

    def calculate_salary(self, bonus=0):
        return self.salary + bonus

    def show_details(self):
        return (
            f"Employee ID : {self.employee_id}\n"
            f"Name        : {self.name}\n"
            f"Department  : {self.department}\n"
            f"Designation : {self.designation}\n"
            f"Salary      : {self.salary}\n"
            f"Email       : {self.email}\n"
            f"Joining Date: {self.joining_date}\n"
            f"Experience  : {self.experience} years"
        )


emp1 = Employee(101, "Gurman", "AI/ML", "Developer",
                50000, "gurman@gmail.com", "01-07-2024", 2)

emp2 = Employee(102, "Avantika", "HR", "HR Manager",
                60000, "avantika@gmail.com", "15-06-2023", 4)

emp3 = Employee(103, "Ritik", "Finance", "Accountant",
                45000, "ritik@gmail.com", "10-01-2022", 5)

emp4 = Employee(104, "Soham", "Marketing", "Executive",
                40000, "soham@gmail.com", "20-08-2024", 1)

emp5 = Employee(105, "Jaado", "IT", "System Admin",
                55000, "jaado@gmail.com", "12-09-2021", 6)


print(emp1.login())
print(emp2.apply_leave(3))
print("Salary:", emp3.calculate_salary())
print("Salary with Bonus:", emp4.calculate_salary(5000))
print()
print(emp5.show_details())