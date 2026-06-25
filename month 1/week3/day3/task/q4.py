def squares(x):
    for i in x:
        yield i*i
x=[1,7,4,8,5,9,4,6,9]        
z=squares(x)

for ir in z:
    print(ir)