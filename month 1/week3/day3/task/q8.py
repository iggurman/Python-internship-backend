def wordsfrom(lst):
    for word in lst:
        yield word[::1]


words = ["python", "java", "hello", "world"]

for i in wordsfrom(words):
    print(i)