
# Take 5 student names in a list and search for a specific student name.
# If found print:
# Student Found
# otherwise:
# Student Not Found

students=[]
for i in range(5):
    a=input("Enter students name ")
    students.append(a)
print(students)

search=input("Search student ")
if search in students:
    print("Student found! ")
else:
    print("Student not found ")