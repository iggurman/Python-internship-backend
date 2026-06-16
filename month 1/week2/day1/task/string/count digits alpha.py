# Take a string from the user and count:
# Alphabets 
# Digits 
# Special Characters 
# Example:
# Input: Python123@
# Output:
# Alphabets = 6
# Digits = 3
# Special Characters = 1

alpha=[]
digi=[]
special=[]

string1=input("enter a string")
for char in string1:
    if char.isalpha:
        alpha.append(char)
    elif char.isnumeric:
        digi.append(char)
    else:
        special.append(char)

print("alpha=",len(alpha))
print("digits=",len(digi))
print("special=",len(special))
        