    # • Count vowels using a set. 

set1=set()

for ele in range(5):
    a=input("enter char")
    
    count=0
    for ch in a:
        if ch in "aeiou":
            count+=1
            set1.add(a)
    print(a,"=",count)       
print(set1)

