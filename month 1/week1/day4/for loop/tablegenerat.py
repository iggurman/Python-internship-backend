# Create a table generator program.
num=int(input("Enter number for generating table "))
i=1
while i<10:
    table=num*i
    print(num, "x", i ,"=", table) 
    i=i+1
    
#for loop
num=int(input("Enter number for generating table "))
for i in range (1,11,1):
    table= num*i
    print(num, "x", i ,"=", table) 
    i+=1