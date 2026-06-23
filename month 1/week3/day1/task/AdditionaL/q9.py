pri=[i for i in range(1,101)if i>1 and all(i%j!=0 for j in range(2,i))]
print(pri)