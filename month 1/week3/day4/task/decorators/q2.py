def decorator(n):
    def actual(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return actual

@decorator(3)
def greet():
    print("hello")
    
greet()
    