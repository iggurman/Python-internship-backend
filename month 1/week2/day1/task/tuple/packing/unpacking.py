# Create a tuple containing:
# Name
# Age
# City
# Course
# Use tuple unpacking and print each value separately.

name=input("enter name ")
age=int(input("enter age "))
city=input("enter city ")
course=input("enter course ")

tuple1=(name,age,city,course)
name, age, city, course, = tuple1

print(f"Name: {name}")
print(f"Name:{age}")
print(f"Name:{city}")
print(f"Name:{course}")
