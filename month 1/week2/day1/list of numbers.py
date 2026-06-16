# Create a list of numbers and print only odd numbers.

list1=[]
for i in range(10):
    a=int(input("enter number"))
    if a%2!=0:
            list1.append(a)
    else:
        continue
print(list1)
