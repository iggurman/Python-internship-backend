def chunk(lst, k):
    for i in range(0, len(lst), k):
        yield lst[i:i+k]

# Example
lst = [1, 2, 3, 4, 5, 6, 7]

for ch in chunk(lst, 3):
    print(ch)