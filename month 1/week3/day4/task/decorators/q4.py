def decorator(func):
    def wrapper(*args,**kwargs):
        print("func name ",func.__name__)
        print("positional ",args)
        print("keyword ",kwargs)
        result= func(*args,**kwargs)
        return result
    return wrapper

@decorator
def add(a,b,c=10,d=20):
    return a+b
print(add(11,22,c=10,d=100))
