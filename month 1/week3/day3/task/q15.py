def asci(x):
    for char in x:
        yield ord(char)
        
x=asci("gurman")
for i in x:
    print(i)