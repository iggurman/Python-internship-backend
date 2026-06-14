# Print odd numbers only.
n=int(input("Enter number till which you want to print odd numbers "))
for i in range(1,n+2):
    if i%2==0:
        continue
    print(i)
    
#using while loop
n=int(input("Enter number till which you want to print odd numbers "))
i=1
while i<n:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1