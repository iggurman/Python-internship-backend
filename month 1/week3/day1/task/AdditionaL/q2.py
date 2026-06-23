dict={
    i:i**2 
    for i in range(1,101)
    if all(i%n!=0 for n in range(2,i))}
print(dict)