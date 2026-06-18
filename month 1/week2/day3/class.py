"""
python virtual machine

when the source code converts to byte code (interpreter) and then to convert to machine code thats what python virtual machine does but executes at run time only!
python becomes slow  because of gil that execute line by line which makes it slow 

python has refrence counting and everything is object
"""
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # Outputs 2 because the reference count includes the argument to getrefcount
b = a
print(sys.getrefcount(a))  # Outputs 3

c = a
print(sys.getrefcount(a))  # Outputs 4

del b
print(sys.getrefcount(a))  # Outputs 3

del c
print(sys.getrefcount(a))  # Outputs 2

del a
# The reference count drops to 1, but because sys.getrefcount was called, the object is still in scope within that call
"""
memory management
stack mem and heap 
value stored in heap and address in stack 
heap is permanent and objects are stored in heap memory and the variables that refers the values address are stored in stack

""" 
import time
start=time.time()
def task():
    for i in range(5):
        print(i)
        time.sleep(1)
        
task()
print(time.time()-start)

# Garbage Collection: Python’s garbage collector complements reference counting by detecting and collecting objects involved in reference cycles. The garbage collector is part of the gc module, which provides the functionality to tune and control garbage collection.
import gc

gc.collect()  # Forces garbage collection

# Raw Memory Allocator: This allocator interacts directly with the underlying operating system to allocate and deallocate memory blocks. It is responsible for managing large memory requests and freeing memory back to the system.
# Object-Specific Allocators: These allocators manage memory for specific types of objects, such as integers, strings, and other built-in types. By tailoring the allocation strategy to the needs of specific objects, Python can reduce fragmentation and improve performance.
# Pymalloc: Pymalloc is a specialized allocator designed for small objects (less than 512 bytes). It enhances performance by reducing the overhead associated with frequent memory allocation and deallocation, which is common in Python programs.
import sys

# Creating multiple small objects
small_int1 = 10
small_int2 = 10
small_int3 = 10

print(sys.getsizeof(small_int1))  # Size of the integer object
print(sys.getsizeof(small_int2))  # Size of the integer object
print(sys.getsizeof(small_int3))  # Size of the integer object

"""
"""