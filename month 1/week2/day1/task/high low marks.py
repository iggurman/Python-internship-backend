#  Take 5 marks from the user and store them in a list. Calculate:
# Total
# Average
# Highest Marks
# Lowest Marks
marks=[]
for i in range(5):
    marks=int(input("enter number"))
    marks.append(i)
print(marks)

print(sum(marks))
print(sum(marks)/len(marks))
print(max(marks))
print(min(marks))
