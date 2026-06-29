class ATM:
    def __init__(self, account_number, card_number, pin,
                balance, account_holder, bank_name,
                branch, ATM_location):
        self.account_number = account_number
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.branch = branch
        self.ATM_location = ATM_location

    def withdraw_cash(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return f"₹{amount} withdrawn successfully. Remaining Balance: ₹{self.balance}"

    def deposit_cash(self, amount):
        self.balance += amount
        return f"₹{amount} deposited successfully. Current Balance: ₹{self.balance}"

    def check_balance(self):
        return f"Available Balance: ₹{self.balance}"

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "PIN changed successfully."

    def mini_statement(self):
        return (
            f"Account Number : {self.account_number}\n"
            f"Account Holder : {self.account_holder}\n"
            f"Bank Name      : {self.bank_name}\n"
            f"Branch         : {self.branch}\n"
            f"ATM Location   : {self.ATM_location}\n"
            f"Current Balance: ₹{self.balance}"
        )


atm1 = ATM(1001, "1234-5678-9012", 1234,
        50000, "Gurman", "SBI",
        "Indore", "Vijay Nagar")

atm2 = ATM(1002, "2345-6789-0123", 4321,
        80000, "Avantika", "HDFC",
        "Bhopal", "MP Nagar")

atm3 = ATM(1003, "3456-7890-1234", 1111,
        35000, "Ritik", "ICICI",
        "Mumbai", "Andheri")

atm4 = ATM(1004, "4567-8901-2345", 2222,
        90000, "Soham", "Axis",
        "Surat", "City Light")

atm5 = ATM(1005, "5678-9012-3456", 3333,
        45000, "Jaado", "Kotak",
        "Delhi", "Connaught Place")


print(atm1.withdraw_cash(5000))
print(atm2.deposit_cash(10000))
print(atm3.check_balance())
print(atm4.change_pin(5555))
print()
print(atm5.mini_statement())