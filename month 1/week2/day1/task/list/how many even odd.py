# Create a list of 10 numbers and count how many numbers are even and odd.
list1=[]
for i in range(10):
    a=int(input("enter number"))
    list1.append(a)
print(list1)

even_count=0
odd_count=0
for num in list1:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"""Even count is {even_count}
odd count is {odd_count}""")