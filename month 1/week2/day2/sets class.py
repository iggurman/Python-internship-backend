# sets are mutable stores unique values and unoredered, does not allow indexing

num={1,2,3,4,5,5,6,6,7,8,65,4,3}
num.add(7050) #adds only 1 value
num.remove(1)#remove only single value but gives error if value not exists
num.discard(1000) #even if value not exists no error will occur and its safe method
num.update({55})  #just like extends


print(num)

a={2,2,3,5,9,6,5}
b={2,3,100,200,300,400}
print(a|b)      #union

print(a & b)      #intersection

print (a-b)     #difference (subtracts the values                that are comman and prints the uniques of first set that 2nd set does not have)

#semantic diff returns both sets remaining values and subtracts the comman values
