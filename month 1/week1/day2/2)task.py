# Check positive/negative number

num1= int(input("Enter the Number to check if its positive or negative "))

if num1>0:
    print(num1,"is a Positive number ")
elif num1<0:
    print(num1,"is a Negative number ")
else :
    print(num1,"is neither positive nor negative")
    
    
# Even or Odd
num2= int(input("Enter Number to check is its Even Or Odd "))

if num2%2==0:
    print(num2,"is an Even Number")
else:
    print(num2,"is an Odd Number")

# Eligible for Voting,Pass or Fail
age=int(input("Enter Age for voting "))

if age>=18:
    print("You are eligible to vote because you are",age)
else:
    print("you are not eligible to vote because you are",age)
    
# Check whether first number is greater and smaller than second
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))

if a>b:
    print("1st number is greater as",a,"is greater than",b)
else:
    print("2nd Number is greater than 1st as",b,"is greater than",a)
    
# Check whether a number is divisible by 10 or 5
num3=int(input("Enter Number to check if its divisible by 5 or 10 "))

if num3 % 10 == 0:
    print("This number is divisible by both 5 and 10")
elif num3 % 5 == 0:
    print("This number is divisible by 5 only")
else:
    print(num3, "is not divisible by 5 or 10")

# Check whether a number is a multiple of 7

num4=int(input("enter number to check if its divisible by 7 "))

if num4%7==0:
    print(num4,"is divisible by 7")
else:
    print(num4, "is not divisible by 7" )

# Check login eligibility:
# Username = admin
# Password = 1234

user=str(input("Enter Username "))
password=int(input ("Enter password "))

if user=="admin":
    if password==1234:
        print("Access Granted")
        
    else:
        print("invalid password")
else:
    print("invalid Username ")

# Check scholarship eligibility:
# Marks ≥ 80 AND Attendance ≥ 75

mark=int(input("Enter your Marks "))
attendance=int(input("Enter your Attendance "))

if mark >= 80 and attendance >= 75:
    print("Eligible for a Scholarship")

elif mark >= 80 and attendance < 75:
    print("Due to less attendance, not eligible for a scholarship")

elif mark < 80 and attendance >= 75:
    print("Due to less marks, not eligible for a scholarship")

else:
    print("Due to less marks and attendance, not eligible for a scholarship")


# Check admission eligibility:
# Marks ≥ 60 OR Sports Certificate = Yes

marks=int(input("Enter Your Marks "))
certificate=input("Do you have a certificate (Yes/No) ")

if marks>=60 or certificate==("yes"or"Yes"):
    print("Admission Granted")
else:
    print("Sorry not eligible for the admission")
    
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
    
# ATM Machine Simulation Menu:
bal=float(input("Enter Your balance "))
print("1. Check balance")
print("2. Withdraw money")
print("3. Deposit money")
print("4. Exit")

option=int(input("Enter your option "))

if option==1:
    print("Current balance is ",bal)
elif option==2:
    withdraw=float(input("Enter your withdrawal amount "))
    if withdraw>bal:
        print("Insufficient Funds!!")
    else:
        print("Withdrawal Successful. Remaining balance left is",bal-withdraw)
elif option==3:
    deposit=float(input("Enter Deposit Amount "))
    if deposit>0:
        print("Deposit successful. New balance is",bal+deposit)
    else:
        print("Invalid amount!")
elif option==4:
    print("Thank you for using ATM")
else:
    print("Invalid Operation")
    
    
