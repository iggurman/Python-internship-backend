# list1,tuple,set,dict all are collective datatypes all are iterables(collection of data)

for i in range(1,11):
    print(i)

#here i is an iterator - its an object, fetches value one at a time
#iterator protocol:iter()(that return iterator object) and next()(returns the next value)
list1=[1,2,3,4,5,6,7,8,9,10]
it=iter(list1)
print(it)#<list1_iterator object at 0x000002968FD50D00>
print(next(it))# returns 1
print(next(it))# returns 2
print(next(it))# returns 3
print(next(it))# returns 4
print(next(it))# returns 5
print(next(it))# returns 6
print(next(it))# returns 7
print(next(it))# returns 8
print(next(it))# returns 9
print(next(it))# returns 10
# print(next(it))# return exceptions StopIteration
# since loops does not give exceptions thats why we use loops because while using iterators we might get stopiteration and also we use iterators for memory efficiency

it = iter(list1)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break

# why we use iterators?
# memory efficiency--instead of loading an entire dataset into memory at once, an iterator calculates and returns one item at a time    
# uniform interface-(not data specific we can use any data type it will execute) loop through diff kinds of data using for loop
# decoupled traversal state:data objects stores only the data, store current value and move to the next value

#custom iterators- init(which is a constructor and initialize values )
#init(start,stop),iter(),next()
# when ever we create a class-call constructor and initialize values 
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

c = Counter(1, 5)
iterator = iter(c)
for i in c:
    print(i)#gives infinite value if we cantdont specify stop value
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break#manual hard coded method
print("--------------generator-------------")
#generator
def couter(max_value):
    count=1
    while count<=max_value:
        yield count
        count+=1
x=couter(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))#why we use gene so that we can access value one by one and also if dont want to store the values
# generator value is executed and only then it  releases memory by yield(returns value and always used in gen)  
# #if i call again i might get stop iteration exception
# that why we use loops 
