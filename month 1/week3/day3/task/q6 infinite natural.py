def infinite(n):
    while True:
        yield n
        n+=1
n=1
x=infinite(n)
for i in x:
    print(i)