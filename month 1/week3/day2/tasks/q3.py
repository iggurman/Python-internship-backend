class odd():
    def __init__(self, start, stop):
        self.current=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        while self.current<self.stop:
            value=self.current
            self.current+=1
            if value%2!=0:
                return value
        raise StopIteration



x=odd(1,20)
for i in x:
    print(i)