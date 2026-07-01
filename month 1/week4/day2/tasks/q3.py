class Employee():
    def __init__(self,employee_id,salary):
        self.__employee_id=employee_id
        if salary<0:
            raise ValueError
        else:
            self.__salary=salary
            
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        if salary<0:
            raise ValueError
        else:
            self.__salary=salary
            return self.__salary
            
            
x=Employee(1001,11111111)
print(x.get_salary())
print(x.set_salary(100000000))
