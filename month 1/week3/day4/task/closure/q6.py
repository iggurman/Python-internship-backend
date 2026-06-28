def outer():

    x = 10

    def inner():
        nonlocal x
        x += 5
        print(x)

    return inner


a = outer()

a()
a()