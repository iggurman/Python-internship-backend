def is_palindrome(x):
    rev=""
    for char in x:
        rev=char+rev
    if rev==x:
        return x,"is palindrome"
    else:
        return x,"is not palindrome"

x=input("enter a string ")
print(is_palindrome(x))