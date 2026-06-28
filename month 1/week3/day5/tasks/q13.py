class BalanceError(Exception):
    pass


balance = 10000

try:

    amount = int(input("Enter Amount: "))

    if amount > balance:
        raise BalanceError("Insufficient Balance")

    balance -= amount

    print(balance)

except BalanceError as e:
    print(e)