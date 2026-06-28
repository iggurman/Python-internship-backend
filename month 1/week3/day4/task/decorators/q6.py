def decorator(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))
print(add(30, 40))
print(add(50, 60))

print("Function called:", add.count, "times")