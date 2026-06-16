subjects = []
marks = []

for i in range(5):
    subject = input("Enter subject name: ")
    subjects.append(subject)

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("Total Marks:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

if average >= 35:
    print("Result : PASS")
else:
    print("Result : FAIL")