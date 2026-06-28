password = "gurman1111"

for i in range(3):

    p = input("Enter Password: ")

    if p == password:
        print("Login Successful")
        break

else:
    print("Account Locked")