class Employee:
    def __init__(self, salary, department):
        departments = ["HR", "IT", "Sales", "Finance"]

        self.__salary = salary

        if department not in departments:
            raise ValueError("Invalid Department")

        self.__department = department

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_department(self):
        return self.__department

    def set_department(self, department):
        departments = ["HR", "IT", "Sales", "Finance"]

        if department not in departments:
            raise ValueError("Invalid Department")

        self.__department = department
        
x=Employee(50000,"IT")
print(x.get_salary())
print(x.get_department())
print(x.set_salary(1000))