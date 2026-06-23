nested = [[1, 2], [3, 4], [5, 6]]
hi=[i for sublist in nested for i in sublist]
print(hi)