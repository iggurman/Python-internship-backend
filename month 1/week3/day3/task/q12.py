def cumsum(x):
    total=0
    for i in x:
        total+=i
    yield total
h=[1,2,3,4,5,6,7,8,9]
j=cumsum(h)
for i in j:
    print(i)