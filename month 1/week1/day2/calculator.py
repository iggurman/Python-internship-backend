#calculator add sub multi divide
num9=int(input("enter the 1st number "))
num10=int(input("enter the 2nd number "))

print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")

choice=int(input("Enter your option "))

if choice==1:
    print("Sum of both is",num9+num10)
elif choice==2:
    print("subtraction of both is",num9-num10)
elif choice==3:
    print("Product of both is",num9*num10)
elif choice==4:
    print("Division of both is",num9/num10)
else:
    print("try again")
    if num10==0:
        print("cannot divide by 0")
