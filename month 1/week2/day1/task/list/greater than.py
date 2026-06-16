# Create a list of 10 numbers and create a new list containing only numbers greater than 25.
# Example:
# Input: [10,20,30,40]
# Output: [30,40]

numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

new_list = []

for num in numbers:
    if num > 25:
        new_list.append(num)

print(new_list)