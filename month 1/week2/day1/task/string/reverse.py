# Take a string and print it in reverse order without using slicing ([::-1]).
# Example:
# Input: Python
# Output: nohtyP

string1=input("enter string")
n=len(string1)

while n>0:
    print(string1[n-1],end=" ")
    n-=1
