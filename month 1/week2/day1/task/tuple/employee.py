# Create a tuple of employee names and check whether a given employee name exists in the tuple.
# Example:
# Input: demo
# Output:
# Employee Found

employees = ("a", "b", "f", "d", "c")

name = input("Enter employee name: ")

if name in employees:
    print("Employee Found")
else:
    print("Employee Not Found")