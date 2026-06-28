while True:

    try:
        n = int(input("Enter integer: "))
        break

    except ValueError:
        print("Try Again")

print(n)