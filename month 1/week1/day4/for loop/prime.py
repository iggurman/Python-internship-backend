#Check whether a number is prime.
num = int(input("Enter a number: "))

count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print("Prime")
else:
    print("Not Prime")

#print prime from 1 to 100
for num in range(2, 101):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)

