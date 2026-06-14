# Search a number in a list and stop when found.
# normally
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num=int(input("search number "))
if num in list:
    print(list,num,"Present")
else:
    print("Not Found")


# using loop 
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num=int(input("search number "))
for i in list:
    if i==num in list:
        print("Found")
        break
    else:
        print("Not Found")
