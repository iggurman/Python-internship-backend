
# deposit withrdawal and total bal

class Bank_account():
    def __init__(self,name,accno,bal,ifsc,address,branch):
        self.name=name
        self.accno=accno
        self.bal=bal
        self.ifsc=ifsc
        self.address=address
        self.branch=branch
        
    def deposit(self,amount,):
        self.bal+=amount
        return self.bal
    
        
    def withdrawal(self,amount):
        if amount>self.bal:
            print("insufficient balance ")
        else:
            self.bal-=amount
        return self.bal
        
        
    def totalbalance(self):
        return self.bal


obj1 = Bank_account("gurman", 100001837, 30000, "sbi7893", "indore", "abc")
print(obj1.deposit(5000))

obj2 = Bank_account("avantika", 100001837, 100000, "hdfc7893", "bhopal", "abc")
print(obj2.withdrawal(2000))

obj3 = Bank_account("jaado", 100001837, 5000, "icic7893", "mumbai", "mnb")
print(obj3.totalbalance())

obj4 = Bank_account("ritik", 100001837, 60000, "kotak7893", "kolkatta", "kdc")
print(obj4.withdrawal(10000))

obj5 = Bank_account("soham", 100001837, 50000, "sbi7893", "surat", "kuf")
print(obj5.totalbalance())