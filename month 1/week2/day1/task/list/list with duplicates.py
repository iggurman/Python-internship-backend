# Create a list with duplicate values and remove duplicates without using set().
# Example:
# Input: [1,2,2,3,4,4,5]

# Output: [1,2,3,4,5]

list1=[]
for i in range(1,11):
    a=int(input(f"enter number {i} "))
    list1.append(a)
print(list1)


for num in list1:
    if list1.count(num)<=1:
        continue
    else:
        list1.remove(num)
        
print(list1)