def decorator(a):
    def wrapper():
        print("before function")
        a()
        print("after function")
    return wrapper

@decorator 
def message():
    print("hello")
message()