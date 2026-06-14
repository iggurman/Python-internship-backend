# Print numbers from 1 to 50 except multiples of 5.
for i in range(1,50):
    if i%5==0:
        continue
    print(i)


# while loop
i=1
while i<50:
    if i%5==0:
        i+=1
        continue
    print(i)
    i+=1