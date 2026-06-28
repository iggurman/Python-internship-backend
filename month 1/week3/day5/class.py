"""
exception disturbs the normal flow of program
exception handling-exception handling is a mechanism used to handle runtine error so that the program does not crash unexpectiedly

try:-the code that may generate an exception is written inside
except:- this block executes only when an exception occurs and can use multiple except block 
else--
finally- used for file handling and cleanup and will get executed everytime
"""
# try:
#     num =int(input("enter number "))
#     x=100//num
#     x=x+1
# except ZeroDivisionError:
#     print("cannot divide by zero ")
# except ValueError:
#     print("enter correct value ")
# else:
#     x=x+1
#     print("Division successful ")
#     print(x)
# finally:
#     print("always executed ")
    
"""(try)if any error comes then (except)if no error then(else),(finally)
"""

# #file
# file=None
# try:
#     file=open("data.txt")
#     file.write()
    
# except FileNotFoundError:
#     print("file not found ")

# finally:
#     if file:
#         file.close()
#     print("File closed")
    
    
#excxeptions
"""ValueError-wrong value entered reuired is int but input is String 
TypeError-wrong datatype
NameError-variable not found
IndexError-invalid index 
KeyError-invalid dictionary key
ZeroDivisionError-divide by Zero
FileNotFoundError-
ImportError-
PermissionError-
RuntimeError-when error comes at runtime
MemoryError-when memory full and crashes  """
# try:
#     dict={1:2,3:4}
#     print(dict["xyz"])
# except KeyError as e:
#     print("wrong value",e)

# try:
#     file=open("demo.txt")
# except KeyError as e:
#     print("wrong value",e)

"""custom exceptions- we can create our own exceptions by inherting from exceptions

"""
class AgeError(Exception):
    pass
try:
    age=23
    if age<18:
        raise AgeError("age must be at least 10 ")

except AgeError as e:
    print("error",e)
    
    
# hierarchy:---system level
# base exception---
# sub which is inhertited from exception:-ArithmeticError:ZeroDivisionError,OverflowError
#             LookupError:IndexError,KeyError
#             ValueError
#             RuntimeError
#             ImportError:ModuleNotFoundError
#             FileNotFoundError