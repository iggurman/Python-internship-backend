# Create a list of 10 numbers and print all numbers greater than 50.
#by creating a new list and adding elements in that or 
list1=[1,2,3,4,50,60,70,80,90,100]
final=[]
for i in list1:
    if i>50:
        final.append(i)

print(f"numbers greater than 50 are {final}")

#by removing elements in that list by making list copy
list1=[1,2,3,4,50,60,70,80,90,100]
for i in list1[:]:
    if i<50:                                                                    
        list1.remove(i)

print(f"numbers greater than 50 are {list1}")