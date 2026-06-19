# ==========================================================
# PYTHON FUNCTIONS
# ==========================================================

# Functions are reusable blocks of code that perform a specific task.
# Once a function is defined, it can be called multiple times.
# Functions help reduce code duplication and improve readability.
# Python provides built-in functions such as print(), len(), sum(), etc.
# We can create our own functions using the 'def' keyword.

# Syntax:
# def function_name(parameters):
#     function body
#     return value


# ==========================================================
# FUNCTION WITHOUT RETURN
# ==========================================================

def add(a, b):
    # a and b are parameters
    c = a + b
    print(c)

# 20 and 30 are arguments
result = add(20, 30)

# Since there is no return statement,
# Python automatically returns None
print(result)


# ==========================================================
# FUNCTION WITH RETURN
# ==========================================================

def multiply(a, b):
    c = a * b
    return c

result = multiply(20, 30)
print(result)


# ==========================================================
# SCOPE
# ==========================================================

# Global Scope
x = 100

def demo():
    # Local Scope
    y = 50
    print("Local Variable:", y)

demo()

print("Global Variable:", x)

# Local variables can only be accessed inside the function.
# Global variables can be accessed throughout the program.


# ==========================================================
# TYPES OF ARGUMENTS
# ==========================================================

# ----------------------------------------------------------
# 1. POSITIONAL ARGUMENTS
# ----------------------------------------------------------
# Arguments are assigned according to their position.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Rules:
# 1. Number of arguments must match parameters.
# 2. Order must be maintained.


# ----------------------------------------------------------
# 2. KEYWORD ARGUMENTS
# ----------------------------------------------------------
# Arguments are passed using parameter names.

def multiply(m, n):
    print(m * n)

multiply(n=10, m=5)

# Rules:
# 1. Order does not matter.
# 2. Parameter names must be specified.


# ----------------------------------------------------------
# 3. DEFAULT ARGUMENTS
# ----------------------------------------------------------
# Parameters can have default values.

def multiply(a=10, b=50):
    return a * b

print(multiply())        # 10 * 50 = 500
print(multiply(5))       # 5 * 50 = 250
print(multiply(5, 10))   # 5 * 10 = 50


# ----------------------------------------------------------
# 4. ARBITRARY POSITIONAL ARGUMENTS (*args)
# ----------------------------------------------------------
# Used when the number of arguments is unknown.
# *args stores all values inside a tuple.

def add(*args):
    print(args)      # tuple
    print(sum(args))

add(20, 30, 40, 50, 60)

# Output:
# (20, 30, 40, 50, 60)
# 200


# ----------------------------------------------------------
# 5. ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# ----------------------------------------------------------
# Used when the number of keyword arguments is unknown.
# **kwargs stores data in a dictionary.

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(name="Demo", age=22, city="Bhopal")

def add(**kwargs):
    res=0
    for key,value in kwargs.items():
        res+=(value)
    print(res)
add(a=20,b=22,c=40)

# Output:
# name : Demo
# age : 22
# city : Bhopal


# ==========================================================
# PARAMETERS VS ARGUMENTS
# ==========================================================

def add(a, b):
    return a + b

# Parameters:
# a, b

add(10, 20)

# Arguments:
# 10, 20


# ==========================================================
# IMPORTANT INTERVIEW POINTS
# ==========================================================

# 1. Functions are first-class objects in Python.
# 2. Every function returns a value.
# 3. If no return statement is used, Python returns None.
# 4. *args stores extra positional arguments as a tuple.
# 5. **kwargs stores extra keyword arguments as a dictionary.
# 6. Local variables exist only during function execution.
# 7. Global variables can be accessed throughout the program.
# 8. Parameters are defined in the function definition.
# 9. Arguments are passed during the function call.

# #lambda functions
# lambda argument:variable=lambda arguments: expression or operation

x= lambda a,b:a+b
print(x(3,4))

x= lambda a:"even" if a%2==0 else "odd"
print(x(3))

list1=[1,2,3,4,4]
res=list(map(lambda x:x*x,list1))
print(res)

#map- function creates a new list or tuple by applying a function to every element of an iterable 
# syntax --map (function,iterable)
#used for transformers

list1=[1,2,3,4,4]
res=map(lambda x:x*x,list1)
print(res)

#filter= if we want to filter a datatype and select elements based on a condition
list1=[1,2,3,4,4]
res=filter(lambda x:x*x,list1)
print(res)

# reducer-multiple values into a single value. collective datatypes returns a single value
#used for aggregate functions 
from functools import reduce

list1=[1,2,3,4,4]
res=reduce(lambda x,y:x+y,list1)
print(res)

list1=[1,2,3,4,4]
res=reduce(lambda x,y:x if x>y else y,list1)
print(res)

student=[("demo",55),("de",55),("deo",99),("demo",89)]
result = filter(lambda x: x[1] >= 75, student)
print(list(result))