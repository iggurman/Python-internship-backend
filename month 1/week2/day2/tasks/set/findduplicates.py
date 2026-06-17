    # • Find duplicate numbers using sets. 
list1=[]
set1=set()
m=int(input("enter total of numbers "))
for i in range(m):
    a=int(input("Enter the number"))
    list1.append(a)
count=0
for a in list1:
    if list1.count(a)>1:
        set1.add(a)
print(set1)
    