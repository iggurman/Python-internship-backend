# Take a string and create a new string containing only the even index characters.
# Example:
# Input: Python
# Output: Pto

old_string=input("Enter the string ")

for i in range(len(old_string)):
    if i%2==0:
        print(old_string[i],end="")

