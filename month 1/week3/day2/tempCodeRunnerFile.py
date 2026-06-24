it=iter(list1)#create a variable to traverse over the iterable
while True:
    try:
        i=next(i)# goes to the next i value
        print(i)# prints the next i
    except StopIteration: #when no more i values/end of iteration   
        break
    