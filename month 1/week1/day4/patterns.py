for i in range (6,1,-1):
    print("*"*i)
for i in range(1,7):
    print("*"*i)
print("-----------------------------")

#nested loop
for i in range(1,6):
    for j in range(0,i):
        print("*",end="")
    print()
for i in range(6,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print("-------------------------------")

for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()
print("---------------------------------")

for i in range(1,6):
    for j in range(i):
            print("*",end="")
    print()
print("------------------------------")

for i in range(6,0,-1):
    for j in range(i):
            print("*",end="")
    print()

print("---------------------------")
for i in range(1,7,1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("---------------------------")

for i in range(7,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()
print("-------------------------")
for i in range(0,6):
    for j in range(i+1):
        print(chr(97+i),end="")
    print()
print("-------------------------")
for i in range(0,6):
    for j in range(i):
        print(chr(97+j),end="")
    print()
print("-------------------------")
for i in range(5,0,-1):
    for j in range(i):
        print(chr(97+j),end="")
    print()