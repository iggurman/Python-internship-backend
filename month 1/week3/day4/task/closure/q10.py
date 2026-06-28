def counter():

    value = 0

    def inc():
        nonlocal value
        value += 1
        return value

    def dec():
        nonlocal value
        value -= 1
        return value

    return inc, dec


increase, decrease = counter()

print(increase())
print(increase())
print(decrease())
print(increase())