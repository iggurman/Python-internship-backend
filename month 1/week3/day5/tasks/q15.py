try:

    marks = int(input("Enter Marks: "))

    if marks < 0:
        raise Exception("Marks Cannot Be Negative")

    if marks > 100:
        raise Exception("Marks Cannot Exceed 100")

    print("Valid Marks")

except Exception as e:
    print(e)