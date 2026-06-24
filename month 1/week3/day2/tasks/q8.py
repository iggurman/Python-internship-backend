"""
8. Why does __iter__() usually return self in most custom iterator implementations?

ans:-because iter() is a dunder method that is used to iterate over the iterables 
if an object has both methods then it is called an iterator
eg a list is not an iterator on its own
but
"""
nums = [1, 2, 3]

it = iter(nums)
print(next(it))
it is nums #false but it is an iterator
"""
Here it is a separate list iterator object
"""