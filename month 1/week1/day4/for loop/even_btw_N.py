# Count how many even numbers exist between 1 and N.
n=int(input("Enter value of n"))
count=0
for i in range(2,n+1,2):
    count+=1
print("Even numbers from 1 and n is ",count)