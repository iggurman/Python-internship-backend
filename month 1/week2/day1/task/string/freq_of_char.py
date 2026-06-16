# Take a string and print the frequency of each character.
# Example:
# Input: banana

# Output:
# b = 1
# a = 3
# n = 2
#dictionary
string1=input("Enter String")
freq={}
for char in string1:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
for key,value in freq.items():
    print(f"{key}={value}")
    
#using lists
string2=input("Enter String")
freq1=[]

for char in string2:
    if char not in freq1:
        count=string2.count(char)
        print(f"{char}={count}")
        freq1.append(char)