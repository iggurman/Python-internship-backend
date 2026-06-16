# Take 5 names in a list and print them in alphabetical order.
# Example:
# Input:
# ["Ram", "demo", "Mohan"]
# Output:
# ["demo", "Mohan", "Ram"]

names = []

for i in range(5):
    name = input("Enter a name: ")
    names.append(name)

names.sort()

print(names)