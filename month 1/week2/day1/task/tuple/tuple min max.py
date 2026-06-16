# Create a tuple of 10 numbers and find:
# Maximum number
# Minimum number
# Sum of all numbers
list1=[]
for i in range(1,11):
    a=int(input(f"enter number {i} "))
    list1.append(a)
    
    tuple1=tuple(list1)
    
print(tuple1)
print(type(tuple1))

print(min(tuple1))
print(max(tuple1))
print(sum(tuple1))