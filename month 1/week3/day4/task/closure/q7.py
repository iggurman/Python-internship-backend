def multiplier(m):

    def multiply(x):
        return x * m

    return multiply


double = multiplier(2)

triple = multiplier(3)

print(double(10))
print(triple(10))