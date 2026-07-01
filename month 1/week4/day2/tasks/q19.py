class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def add_money(self, amount):
        self.__balance += amount

    def spend_money(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        return self.__balance


w = Wallet(1000)

print(w.check_balance())

w.add_money(500)
print(w.check_balance())

w.spend_money(300)
print(w.check_balance())