"""in oops 1st imp is class and second is object 
oop---object oriented programming is a programming style where we represent real world things as objects """

class Student:
    school_name="agarwal public school" #class attribute ##defined globally so class attribute and single defined and defined in class
    def __init__(self,name,age,dept):
        self.name=name#instance attribute
        self.age=age
        self.dept=dept
        print("constructor called ",self.name)

    def study(self):
        print(f"{self.school_name},{self.name},{self.age},{self.dept}")#accessed class attribute through self 

    def attend_class(self):
        print(self.name,"not attended class")

obj1 = Student("gurman",18,"it")##instance attribute-stores diff objects 
obj1.study()
obj2 = Student("avantika",18,"it")
obj2.attend_class()
obj3 = Student("pranjali",18,"it")
obj3.attend_class()
obj4 = Student("hahah",18,"it")
obj4.attend_class()      
# obj1.study()
"""
class=class is a blueprint or template used to create an object
object=object is a real instance of class which represents a class
constructor=constructor is a special method that automatically gets executed when an object is created 
"""

# deposit withrdawal and total bal

class Bank_account():
    def __init__(self,name,accno,bal,ifsc,address,branch):
        self.name=name
        self.accno=accno
        self.bal=bal
        self.ifsc=ifsc
        self.address=address
        self.branch=branch
        
    def deposit(self,amount,):
        self.bal+=amount
        return self.bal
    
        
    def withdrawal(self,amount):
        if amount>self.bal:
            print("insufficient balance ")
        else:
            self.bal-=amount
        return self.bal
        
        
    def totalbalance(self):
        return self.bal


obj1 = Bank_account("gurman", 100001837, 30000, "sbi7893", "indore", "abc")
print(obj1.deposit(5000))

obj2 = Bank_account("avantika", 100001837, 100000, "hdfc7893", "bhopal", "abc")
print(obj2.withdrawal(2000))

obj3 = Bank_account("jaado", 100001837, 5000, "icic7893", "mumbai", "mnb")
print(obj3.totalbalance())

obj4 = Bank_account("ritik", 100001837, 60000, "kotak7893", "kolkatta", "kdc")
print(obj4.withdrawal(10000))

obj5 = Bank_account("soham", 100001837, 50000, "sbi7893", "surat", "kuf")
print(obj5.totalbalance())