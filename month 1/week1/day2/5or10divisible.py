# Check whether a number is divisible by 10 or 5
num3=int(input("Enter Number to check if its divisible by 5 or 10 "))

if num3 % 10 == 0:
    print("This number is divisible by both 5 and 10")
elif num3 % 5 == 0:
    print("This number is divisible by 5 only")
else:
    print(num3, "is not divisible by 5 or 10")
