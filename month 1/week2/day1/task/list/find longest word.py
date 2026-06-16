# Take a string and find the longest word.
# Example:
# Input: Python is very easy to learn

string1=input("input the string")
string2=string1.split()
longest=string2[0]

for word in string2:
    if len(word)>len(longest):
        longest=word
        
print(f"longest word is {longest}")