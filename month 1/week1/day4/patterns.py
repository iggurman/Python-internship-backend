#nested loop
for i in range (6,1,-1):
    print("*"*i)
for i in range(1,7):
    print("*"*i)

for i in range(1,6):
    for j in range(0,i):
        print("*",end="")
    print()
    
    