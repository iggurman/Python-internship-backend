lst = [10,20,30,40,50]

try:
    index = int(input("Enter index: "))
    print(lst[index])

except IndexError:
    print("Invalid Index")