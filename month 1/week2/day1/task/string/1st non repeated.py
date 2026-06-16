# Take a string and find the first non-repeated character.
# Example:
# Input: swiss
# Output:w

string1=input("enter string")
for char in string1:
    if string1.count(char)==1:
        print("1st non repeating character found",char)
        break
    else:
        print("not found")