class NumberIterator:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num==11:
            raise StopIteration
        value=self.num
        self.num+=1
        return value
    
x=NumberIterator()
for i in x:
    print(i)
    
class trial:
    def __init__(self, start, end):
        self.current=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==self.end:
            raise StopIteration
        value=self.current
        self.current+=1
        return value

z=trial(1,11)
for j in z:
    print(j)