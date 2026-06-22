from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]

square=list(map(lambda x:x*x,nums))
even=list(filter(lambda x:x%2==0,nums))
sum=reduce(lambda x,y:x+y,nums)



print(square)
print(even)
print(sum)