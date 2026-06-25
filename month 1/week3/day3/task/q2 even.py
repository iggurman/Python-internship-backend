def even(n):
    for i in range (1,n):
        if i%2==0:
            yield(i)
            
n=int(input("enter a value "))
j=even(n)

for hj in j:
    print(hj)