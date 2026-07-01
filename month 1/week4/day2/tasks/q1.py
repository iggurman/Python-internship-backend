class Student():
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks

    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks ")
    
    def show_details(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)
        
x=Student("Gurman",80)
x.show_details()
x.set_marks(90)
x.show_details()