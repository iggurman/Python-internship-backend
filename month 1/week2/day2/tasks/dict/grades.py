#    • Group students by grade using a dictionary.

dict={}
n=int(input("Enter the number of grades "))
for i in range(n):
    key=input("enter the grades ")
    m=int(input("Enter the number of students that got this grade "))
    dict[key]=[]
    for j in range(m):
        student=input("enter the student's name ")
        dict[key].append(student)
print(dict)