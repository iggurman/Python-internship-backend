class EmployeeAge():
    def __init__(self,age):
        if age<18 or age>60:
            raise ValueError
        else:
            self.__age=age

    @property
    def age(self):
        return self.__age
    
x=EmployeeAge(26)
print(x.age)