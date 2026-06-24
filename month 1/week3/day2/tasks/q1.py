"""
Q1)What methods must a class implement to become an iterator in Python?
answer)class should implement 2 methods:
        1)__iter__-this is used to return the iterator object itself over the iterables(like lists,tuples etc)
        it is called when the iteration begins 
        2)__next__- this is used to print the next value in the sequence
        StopIteration is ued when there are no more values to be printed
eg:---
"""
class NumberIterator:
        def __init__(self):
                self.num=0
                
        def __iter__(self):
                return self
        def __next__(self):
                if self.num==11:
                        raise StopIteration
                value=self.num
                self.num+=1
                return value
        
x=list(NumberIterator())
for i in x:
        print(i)

#prints numbers 1-10