# # Ask user for a password and stop when correct password is entered.
while True:
    password=input("Enter password")
    
    if password=="gurman":
        print("Correct password")
        break
    
    print("Try again")

#3 times password chance
for i in range(3):
    password=input("Enter password")
    if password=="gur":
        break
    print("incorrect password!!! Account is locked")
print("correct")

#user and pass
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Invalid username or password")

if attempts == 3:
    print("Account Locked")