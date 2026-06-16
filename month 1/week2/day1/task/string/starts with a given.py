# Take a string and check whether it starts with a given character.
string=input("enter the string ")
char=input("enter the character ")
if char==string[0]:
    print(f"Yes {string} starts with {char}")
else:
    print(f"No {string} does not start with {char}")