def positive(func):
    def wrapper(*args):
        for i in args:
            if i<=0:
                raise ValueError
        return func(*args)
    return wrapper

@positive
def add(a,b):
    return a+b

print(add(2,3))
print(add(33,5))
print(add(-45,6))