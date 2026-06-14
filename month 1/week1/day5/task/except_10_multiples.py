# Print numbers from 1 to 100 except multiples of 10.
for i in range(1,100):
    if i%10==0:
        continue
    print(i)


#using while loop
i=1
while i<100:
    if i%10==0:
        i+=1
        continue
    print(i)
    i+=1
