def numbers(n):
    for i in range(1,n+1):
        yield (i)

n=int(input("enter a number "))
x=numbers(n)

for j in x:
    print(j)