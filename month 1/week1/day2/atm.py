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
    
    
