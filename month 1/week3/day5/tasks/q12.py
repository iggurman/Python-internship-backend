class SalaryError(Exception):
    pass


try:

    salary = int(input("Enter Salary: "))

    if salary < 20000:
        raise SalaryError("Salary Too Low")

    print("Valid Salary")

except SalaryError as e:
    print(e)