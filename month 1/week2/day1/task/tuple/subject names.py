# Create a tuple of subject names and a list of marks. Print:
# Maths : 90
# English : 85
# Science : 80
# using a loop.

subject=[]
marks=[]
for word in range(3):
    name=input("enter subject names ")
    subject.append(name)

for word in range(3):
    mark=input("enter marks ")
    marks.append(mark)
    
subject=tuple(subject)

for name,mark in zip(subject,marks):
    print(name," ",mark)
