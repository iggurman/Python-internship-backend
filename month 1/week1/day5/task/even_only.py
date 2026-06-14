# Print even numbers only.
n=int(input("enter number till which you want to print even numbers "))
for i in range(1,n+2):
    if i%2!=0:
        continue
    print(i)
    
#while loop
n=int(input("enter number till which you want to print even numbers "))
i=1
while i<n:
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1