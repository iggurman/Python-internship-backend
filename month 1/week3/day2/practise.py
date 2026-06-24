"""

iterable-the collection of datatypes which can be traversed one by one
how does py traverse a iterable?
"""
list1=[1,2,3,4,5]
for i in list1:
    print(i)
"""
now what python does in background is this
"""
# it=iter(list1)#create a variable to traverse over the iterable
# while True:
#     try:
#         i=next(i)# goes to the next i value
#         print(i)# prints the next i
#     except StopIteration: #when no more i values/end of iteration   
#         break
    
"""
Iterator- its an object that provides the value one at a time 
it keeps track of the current value 
"""

nums = [1,2,3]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

