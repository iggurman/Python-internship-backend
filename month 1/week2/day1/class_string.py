# #strings
# multi line strings are called doc strings

str1='hello  ' #space also counts as a character
str2="hello"
str3="""hello
        hello i am gurman
        whatsapp"""
print(str1,str2,str3)

#to print id 
print(id(str1))   

#to print indexing               
print(str1[1])  #indexing is allowed in strings

#assigning values to a new string cause string is immutable
new_str= "m"+str1[1:]
print(new_str)


# its ordered, immutable (once declared it cant be changed )

for i in range(len(str1)-1):
    print(str1[i])

print(str1[-3])
#will print e from helo
# indexing is from 0 to n-1
# negative indexing is start from last at -1


#string Slicing used to extract a part of the sequence of a string
str4="gurman garg" #space will also be counted and is like a range funcṭion
print(str4[0:8:2]) #start:stop:step (colon is important)

#string concat
first="gurman"
last="garg"
str1=first+" "+last #with use of 3rd variable
print(str1)
print(first+" "+last) #without 3rd variable
print("yo"*5) #multiplication of strings 5 times

# string and python both are case sensitive

str5="demo" #both have diff ids but we can create a new string instead of modifying the old one
str5=str5+"demo2"
print(str5)

#check if char is in the string or not
print("m" in str5) # True

# lower
print(str5.lower())
#capitalize 1st
print(str5.capitalize())
#upper case
print(str5.upper())
#strip used to strip the spaces of the string
print(str1.strip)
#replace method used to replace the word in a string
print(str5.replace("demo","python"))
#split used to split words on basis of space(or anything we specify) and adds them to a list
text="python c c++ java"
print(text.split(" "))
#join used to join the strings in a list to convert back to a string
list=["banana","apple","mango"]
print(" ".join(list))

text="this is a python"
print(text.count("a","e"))


count=0
for char in text:
    if char in "aeiou":
        count+=1
print("count")