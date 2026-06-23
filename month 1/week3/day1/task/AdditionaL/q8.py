s=input("enter a string ")
vowel={v:s.count(v) for v in s if v in "aeiou"}
print(vowel)