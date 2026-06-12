#Find the sum of first N natural numbers.
n=int(input("enter number"))
total=0
for i in range(0,n+1,1):
    total=total+i
print("sum of n is",total)