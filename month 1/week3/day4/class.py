# """
# closure function- It is a function object that remembers values from its enclosing scope even after the outer function has finished execution

# nested function:---
# """
# a=10 # global scope
# def outer():    
#     print("outer functions ")
#     y=5 # enclosing scope
    
#     def inner():
#         x=10 # local
#         print("inner functions ")
        
#     print("before inner ")
#     inner()
#     print("after  inner ")
# x=outer()
# print(x)
# print("---------------------------------")

# #LEGB-(Local)(enclosing)(global scope)(built in scope)

# # nonlocal- variable that can update variables values which are assigned and not assigned we can update any variables value

# #decorator-a decorator is a function that modifies or extends the behaviour of another function without chnaging its original code used for authentications of dependence

# def decorator(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
#     return wrapper

# @decorator
# def message():
#     print("hello")
# message()
# print("-----------------------------")
# # wrapper_obj=decorator(message) # or simply use @decorator
# # wrapper_obj()



# def login_required(abc):
#     def wrapper(user):
#         if user == "gurman!":
#             abc(user)
#         else:
#             print("login failed")

#     return wrapper


# @login_required
# def dashboard(user):
#     print("Welcome", user)
# dashboard("gurman")
# print("--------------------------------------")

# # also check the excecution time of any func in a project if project is slow
# import time
# def login_required(abc):
#     def wrapper(user):
#         start=time.time()
#         abc(user)
#         end=time.time()
#         print("Execution line",end-start)

#     return wrapper


# @login_required
# def dashboard(user):
#     print("Welcome", user)


# dashboard([1,2,3,4,5,6,7,8,9])
# print("-----------------------------------")



def validate_positive(a):
    def wrapper(*args):
        for num in args:
            if num <= 0:
                print("Arguments must be positive!") 
            else:
                return a(*args)
    return wrapper


@validate_positive
def square(num):
    return num*num
print(square(-6))

@validate_positive
def rectangle(length,width):
    return length*width
print(rectangle(2,3))
