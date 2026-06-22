def find_max(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return "both are equal "

x=int(input("enter 1st number "))
y=int(input("enter 2nd number "))
z=find_max(x,y)
print(z,"is the greatest")
