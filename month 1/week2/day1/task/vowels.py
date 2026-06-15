# Take a string and count how many vowels (a, e, i, o, u) are present.
text=input("enter string")

count=0
for char in text:
    if char in "a.e.i.o.u":
        count+=1
print(count)

#for consonents 

text=input("enter string")

count=0
for char in text:
    if char not in "a.e.i.o.u":
        count+=1
print(count)