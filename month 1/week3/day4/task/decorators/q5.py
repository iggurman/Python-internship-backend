is_logged_in=input("logged in? ").lower()

def decorator(func):
    def wrapper():
        if is_logged_in == "yes":
            func()
        else:
            print("not logged in ")
        
    return wrapper


@decorator
def check():
    print("yes logged in ")
    
check()
