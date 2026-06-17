#  Calculate total marks from a dictionary. 
dict={}
n=int(input("enter number of subjects"))
for i in range(n):
    subjects=input("Enter subject name ")
    marks=int(input("enter marks of the subject "))
    dict[subjects]=marks
total=sum(marks.values())
print("subjects ", marks())
print("total marks ",total)
avg=total/(len(dict.values))
print("average ",avg)
topper=max(dict.values())
print("topper marks ",[subjects])
