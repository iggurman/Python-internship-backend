class MyRange():
    def __init__(self,start,stop):
        self.current=start
        self.end=stop
        self.index=-1
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>=self.end:
            raise StopIteration
        value=self.current
        self.index+=1
        self.current+=1
        return value,self.index

obj = MyRange(5, 10)
for i in obj:
    print(i)
