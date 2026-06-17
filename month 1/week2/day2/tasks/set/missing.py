    # • Find missing numbers from a set. 
user=set()
number=int(input("number of elements in your set "))
for i in range(number):
    b=input(f"enter number {i+1} ")
    user.add(b)
    
print("original set",user)

set1=set()
n=int(input("enter last number "))
complete=set(range(n+1))
missing=complete-user
print(missing)