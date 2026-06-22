pri=list(range(1,51))
print(pri)
hudhud=list(filter(lambda x:x>1 and all(x%i!=0 and i!=x for i in range(2,x)),pri))
print(hudhud)