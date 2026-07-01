class BankAccount():
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
        
        
    def deposit(self,deposit):
        if deposit<0:
            print("Invalid Amount")
        else:
            self.__balance=self.__balance+deposit
            print( "new balance",self.__balance)
        
    def withdraw(self,withdraw):
        if withdraw<0:
            print("invalid amount withdrawal")
        elif withdraw>self.__balance:
            print("cant withdraw more than available balance ")
        else:
            self.__balance=self.__balance-withdraw
            print( "new balance",self.__balance)
        
    def get_balance(self):
        return self.__balance
    
x=BankAccount(1001001,50000)
x.deposit(50000)
x.withdraw(100)
