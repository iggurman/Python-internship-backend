class reverse:
    def __init__(self, text):
        self.current=text
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<-len(self.current):
            raise StopIteration
        value=self.current[self.index]
        self.index-=1
        return value,self.index
        
        
hero=reverse("python")
for i in hero:
    print(i)