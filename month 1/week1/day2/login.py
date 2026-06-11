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

