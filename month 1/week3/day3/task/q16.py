def alter(x,y):
    for i,j in zip(x,y):
        yield i
        yield j


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

y=alter(list1,list2)
for i in y:
    print(i)