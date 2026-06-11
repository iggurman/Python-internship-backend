a= 5
print(type(a))

b=5.12
print(type(b))

c="hhh"
print(type(c))


a=10
b=11
print(a!=b)

print (a==b and b>a)
print (a==b or b>a)

list=[1,2,3,4,5]
if 10 not in list:
    print("true")
    
else:
    print("false")
    
age= 19  
if age >= 18:
    print("ready")
else:
    print("not ready")
    

a= 10
b=20  
c=20
if a > b and a==c:
    print("a is greater ")
elif c>b:
    print("ggg")
else:
    print("yo")
    

a=100
b=23
c=30

if a>b:
    print("a is greater")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")