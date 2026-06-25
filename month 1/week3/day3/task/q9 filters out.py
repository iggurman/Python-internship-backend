def filters(x):
    for i in range(x):
        if i%2!=0:
            yield i
x=filters(20)
for i in x:
    print(i)