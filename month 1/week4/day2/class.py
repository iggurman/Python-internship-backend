"""
encapsulation-wrapping of data(attributes) and methods(functions) 
Hide the internal data.
Encapsulation is the process of hiding data inside a class and allowing it to be accessed or modified only through the class's methods.
Allow access only through methods.
private public and protected are a part of encap that control the data for directly accessing it and protect the data
eg- atm has withdraw deposit but you cant accesss the data only access the methods
Benefits=data security cause no one can access,hidden data,better control,validation possible
Access MODIfiers:-public(),protected(_name),private(__name)

Public accessed anywhere even outside the class
Protected can only be accessed in class and sub class(but only python allows access outside class so rules should be followed by devs)
Private can be accessed in only same class

"""
class Student:
    def __init__(self):
        self.name="abc"
        
s=Student()
print(s.name)
s.name="xyz"
print(s.name)

"""if we create variables and methods so we want the variable to stay in the same class so we use private access modifier in python"""

class Employee:
    def __init__(self):
        self.__salary=5000
        
    def details(self):
        print(self.__salary)
        
# class Attendence(Employee):
#     def show(self):
#         print(self._salary)
        
emp=Employee()
emp.details()
# at=Attendence()
# at.show()
"""
the pvt attributes we have created we can access using getter and update through setter outside class 
getter is method used to read or retrieve value of a private attribute 
setter is a method used to update the value of a private attribute after validating the input(have to use getter again after setting the value)
"""

class Employee:
    def __init__(self):
        self.__salary=50000
        self.__name="abc"
        
    def get_salary(self):               #getter
        return self.__salary
    def get_name(self):
        return self.__name
    
    def set_salary(self,salary):        #setter
        if salary>0:                    #validation in set
            self.__salary=salary
    def set_name(self,name):
        self.__name=name

emp=Employee()
print(emp.get_salary())
print(emp.get_name())
emp.set_name("gurman")
emp.set_salary(200000)
print(emp.get_salary())
print(emp.get_name())

# property decorator=no need to call it will directly print and kind of like a decorator and reads methods as attributes so no need to call the method

class Employee:
    def __init__(self):
        self.__salary = 50000

    @property
    def get_salary(self):
        return self.__salary
    
    @get_salary.setter
    def update(self,value):
        if value>0:
            self.__salary=value


emp = Employee()
print(emp.get_salary)
emp.update=1000
print(emp.get_salary)