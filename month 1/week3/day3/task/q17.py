def power(x):
    for i in range(x):
        yield 2**i
for num in power(6):
    print(num)