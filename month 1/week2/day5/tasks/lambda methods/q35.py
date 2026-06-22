from functools import reduce
fact=6
hu=reduce(lambda x,n:x*n,range(1,fact+1))
print(hu)