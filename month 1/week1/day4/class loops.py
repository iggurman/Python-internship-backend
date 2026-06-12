# for loop and while loop
list=[10,20,30,40]
print(list)
for num in list:
    print(num)
    
# range () function has start,stop and step and is immutable

list=[10,20,30,40]
print(list)
for num in range(1,len(list),2):
    print(list[num])

# reverse list
list=[10,20,30,40,50]
print(list)
for num in range(len(list)-1,-1,-1):
    print(list[num])
    
