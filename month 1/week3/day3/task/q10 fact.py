def facto(n):
    fa=1
    for i in range(1,n+1):
        fa*=i
        yield fa
for v in facto(5):
    print(v)
