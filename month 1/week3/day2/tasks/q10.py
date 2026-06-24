class Counter():
    def __init__(self,):
        self.current=97
        
    def __iter__(self):
        return self
    def __next__(self):
        value=chr(self.current)
        self.current+=1
        if self.current>122:
            self.current=97
        return value
    
obj = Counter()
for _ in obj:
    print(next(obj))
