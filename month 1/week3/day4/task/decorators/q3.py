import time 
def decorator(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("start time ",start)
        print("end time",end)
        print("execution time ",end-start)
    return wrapper

@decorator
def timepas():
    for i in range(100):
        print(i)

timepas()