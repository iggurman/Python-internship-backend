try:

    n = int(input("Enter Number: "))

    ans = 100/n

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot Divide")

else:
    print(ans)

finally:
    print("Execution Finished")