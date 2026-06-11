#ternary operator- python allows inline conditions using a ternary operator
age=int(input())
result="eligible for vote" if age>=18 and age<100 else "not eligible"
print(result)

# loops 
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

    
for i in range(1,4):
    for j in range (1,4):
        print(i*j,end=" ")
    print()
    
    
#password enter  
password= ""
while password!="Gurman":
    password=input("enter password:")
print("login successful")

# lenght of string in a list
list =["apple","banana","mango"]

for num in list:
 print(len(num))