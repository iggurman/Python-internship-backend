# # Ask user for a password and stop when correct password is entered.
while True:
    password=input("Enter password")
    
    if password=="gurman":
        print("Correct password")
        break
    
    print("Try again")

# #3 times password chance
# for i in range(3):
#     password=input("Enter password")
#     if password=="gur":
#         break
#     print("incorrect")
# print("correct")