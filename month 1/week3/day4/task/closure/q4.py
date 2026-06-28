def account(balance):

    def operation(choice, amount=0):
        nonlocal balance

        if choice == "deposit":
            balance += amount

        elif choice == "withdraw":
            balance -= amount

        elif choice == "check":
            return balance

    return operation


acc = account(1000)

acc("deposit",500)
acc("withdraw",300)

print(acc("check"))