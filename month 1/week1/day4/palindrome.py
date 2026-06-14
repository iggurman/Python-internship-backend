num = int(input("Enter number: "))
a = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if a == rev:
    print("Palindrome")
else:
    print("Not Palindrome")