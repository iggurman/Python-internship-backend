

def add(a, b):
    y = a + b
    return y

x = add(4, 5)
print(x)

print("-------------------------------")
# generator
def counter():
    yield 1
    yield 2
    yield 3

iterator = counter()# create a object
print(next(iterator))
print(next(iterator))
print(next(iterator))
#generators are special ways to produce value one by one 
#instead of creating everything at once
#lazy iterator:is a slow process

print("--------------------------")
def counter():
    for i in range(1,6):
        yield(i)

iterator = counter()# create a object
for i in iterator:
    print(i)
print("-----------------------------------------")
'generators expression--denoted by round brackets () and same as a list compre but generate values one by one ' 

x=(x*x for x in range (1,6))
print(x)
print(next(x))#returns a value one by one 
print(next(x))

#list comprehension 
x=[x*x for x in range (1,6)]
print(x)

"""
yield vs return
return -- used in normal functions and returns a single or collection of data(like a list) at once and
        terminates the function memory usage-high
yield --returns a single value and saves the state and pauses the function memory usage-low

methods of a generator 

send()-=send 1 value into a running generator using g.send(100)
throw()-part of an exception handling,we can throw exceptions using throw method
close()-when values are yielding but we want to terminate the generator functions 
"""
print("-----------send method------------")
def sender():
    while True:
        value=yield
        print("received value ",value)
g=sender()
next(g)
g.send(100)

print("------------throw method-----------")
def demo():
    try:
        yield 1
    except ValueError:
        yield"value Error handled "  
g=demo()
print(next(g))
print(g.throw(ValueError))

print("-----------close method------------")
def he():
    while True:
        yield 1
        yield 2
g=he()
print(next(g))
g.close()
# print(next(g))



"""
closer func
its a function object that remembers values from its enclosing scope after the outer function has finished execution 
"""
print("-----------closer function------------")
x = "abc"

def demos_outer():
    x = "hello"   # enclosing s-cope
    def demos_inner():
        m = 10    # local scope
        print(f"{m} {x}")
    return demos_inner

k = demos_outer()
print(k)#k is an object now
k()
