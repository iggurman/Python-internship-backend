def running_total():

    total = 0

    def add(num):
        nonlocal total
        total += num
        return total

    return add


r = running_total()

print(r(10))
print(r(5))
print(r(8))