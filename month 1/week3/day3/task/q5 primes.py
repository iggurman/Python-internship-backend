# def primes(n):
    
#     for i in range(2,n+1):
#         prime=True
#         for j in range(2,i):
#             if i%j==0:
#                 prime=False
#                 continue
#         if prime:
#             yield(i)

# n=int(input("enter a number "))
# y=primes(n)

# for i in y:
#     print(i)
    
def prime(n):
    for i in range(2,n+1):
        if all(i%j!=0 for j in range(2,i)):
            yield(i)
            
n=int(input("enter a number "))
y=prime(n)
for i in y:
    print(i)