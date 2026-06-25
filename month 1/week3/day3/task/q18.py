import random

def ran(n):
    for _ in range(n):
        yield random.randint(1, 100)

# Example
for num in ran(5):
    print(num)