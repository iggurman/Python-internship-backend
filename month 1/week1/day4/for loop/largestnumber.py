# Find the largest number from 5 user inputs.
largest=int(input("Enter number 1 "))
for i in range(2,4):
    num=int(input(f"Enter Number {i} "))
    if num>largest:
        largest=num
print(f"Largest number is {largest} ")