# • Find common skills among employees.
student1=set()
student2=set()
n=int(input("number of skills of 1st employee "))
m=int(input("number of skills of 2nd employee "))
for i in range(n):
    a=input("skills of student 1 ")
    student1.add(a)
for j in range(m):
    b=input("skills of student 2 ")
    student2.add(b)
    
print(student1)
print(student2)
print(student1 & student2)

