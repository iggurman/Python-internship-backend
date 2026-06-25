def countdown(n):
    for i in range(n,0,-1):
        yield i
x=countdown(20)
for i in x:
    print(i)