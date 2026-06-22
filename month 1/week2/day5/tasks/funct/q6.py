def count_vowels(string):
    count=0
    for char in string:
        if char in "aeiou":
            count+=1
    return count
x=input("enter string ")
print(count_vowels(x))