# Take a string and check whether it contains only digits.
# Example:
# Input: 12345
# Output: Valid Number

string1=input("Enter string")
if string1.isdigit():
    print("valid number")
elif string1.isalpha():
    print("invalid number")
else:
    print("invalid number")