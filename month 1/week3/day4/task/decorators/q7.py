def cached(func):
    dict={}
    def wrapper(*args):
        if args in dict:
            return "already cached",args
        else:
            result=func(*args)
            dict[args]=result
            return result
    return wrapper

@cached
def square(a):
    return a*a


print(square(7))
print(square(7))
print(square(8))
print(square(9))
print(square(8))