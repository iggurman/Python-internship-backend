#using iterator protocol

employees = ["John", "Mike", "Sara", "Alex"]

it=iter(employees)
print(next(it))
print(next(it))
print(next(it))
print(next(it))






class emp():
    def __init__(self, employees):
        self.current=employees
        self.index=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=len(employees):
            raise StopIteration
        value=self.current[self.index]
        self.index+=1
        return value 
            


employees = ["John", "Mike", "Sara", "Alex"]

x=emp(employees)
for chr in x:
    print(chr)