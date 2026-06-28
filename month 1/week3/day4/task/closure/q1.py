def greet(name):

    def message():
        print("Hello", name)

    return message


x = greet("Gurman")
x()