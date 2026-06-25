def reverse(lst):
    for word in lst:
        yield word[::-1]
words=["gurman","is","my","name"]
for i in reverse(words):
    print(list(i))