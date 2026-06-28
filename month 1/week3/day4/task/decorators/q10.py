def dec1(func):
    def wrapper():
        print("dec 1 before ")
        func()
        print("dec 1 after ")
    return wrapper

def dec2(func):
    def wrapper():
        print("dec 2 before ")
        func()
        print("dec 2 after ")
    return wrapper

@dec1
@dec2
def greet():
    print("hello")
    
greet()