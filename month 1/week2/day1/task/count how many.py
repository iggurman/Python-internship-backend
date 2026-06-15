# Take a string and count how many uppercase letters and lowercase letters it contains.
string=input("enter your string ")

lower_count=0

for char in string:
    if char.islower():
        lower_count+=1
print(f"Lower count of {string} is {lower_count}")

upper_count=0

for char in string:
    if char.isupper():
        upper_count+=1
print(f"Upper count of {string} is {upper_count}")


#both with each other 
string=input("Enter String ")
upper=0
lower=0

for char in string:
    if char.islower():
        lower+=1
    elif char.isupper():
        upper+=1
print("Lower case",lower)
print("Upper case",upper)