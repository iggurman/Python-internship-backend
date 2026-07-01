class BankLocker:
    def __init__(self, locker_number):
        self.__locker_number = locker_number

    @property
    def locker_number(self):
        return self.__locker_number

x = BankLocker(101)
print(x.locker_number)
