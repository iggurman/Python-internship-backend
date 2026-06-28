def add(a,b):

    try:
        print(a+b)

    except TypeError:
        print("Incompatible Data Types")


add(10,20)

add(10,[5])