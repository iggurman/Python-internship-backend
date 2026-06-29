class BankAccount:
    def __init__(self, account_number, account_holder, bank_name,
                branch, balance, account_type, IFSC, mobile_number):
        self.account_number = account_number
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.branch = branch
        self.balance = balance
        self.account_type = account_type
        self.IFSC = IFSC
        self.mobile_number = mobile_number

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance

    def transfer_money(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return f"₹{amount} transferred successfully. Remaining Balance: ₹{self.balance}"

    def print_statement(self):
        return (
            f"Account Number : {self.account_number}\n"
            f"Account Holder : {self.account_holder}\n"
            f"Bank Name      : {self.bank_name}\n"
            f"Branch         : {self.branch}\n"
            f"Balance        : ₹{self.balance}\n"
            f"Account Type   : {self.account_type}\n"
            f"IFSC           : {self.IFSC}\n"
            f"Mobile Number  : {self.mobile_number}"
        )


acc1 = BankAccount(1001, "Gurman", "SBI", "Indore",
                50000, "Savings", "SBIN0001234", "9876543210")

acc2 = BankAccount(1002, "Avantika", "HDFC", "Bhopal",
                80000, "Current", "HDFC0005678", "9876501234")

acc3 = BankAccount(1003, "Ritik", "ICICI", "Mumbai",
                35000, "Savings", "ICIC0007890", "9876512345")

acc4 = BankAccount(1004, "Soham", "Axis", "Surat",
                90000, "Current", "UTIB0004321", "9876523456")

acc5 = BankAccount(1005, "Jaado", "Kotak", "Delhi",
                45000, "Savings", "KKBK0001111", "9876534567")


print("Deposit:", acc1.deposit(5000))
print("Withdraw:", acc2.withdraw(10000))
print("Balance:", acc3.check_balance())
print(acc4.transfer_money(15000))
print()
print(acc5.print_statement())