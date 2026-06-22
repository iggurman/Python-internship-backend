from functools import reduce
words=['Python',
    'is',
    'awesome']
resu=(reduce(lambda x,y:x+" "+y,words))
print(resu)