def flatten(y):
    for item in y:
        for value in item:
            yield value
            
y = [[1, 2], [3, 4], [5, 6]]
x=flatten(y)
for i in x:
    print(i)