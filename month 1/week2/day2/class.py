# #list comprehension
# create a new list using a single line we create using an existing list or tuple or can create using a range 

# syntax----list[expression for num in iterable]

list=[]
for i in range(1,6):
    list.append(i)
print(list)

new_list=[i*i for i in range(1,6)]
print(new_list)

new_list=[i for i in range(1,20) if i%2==0]             # ]
print(new_list)                                         # ]turnery operator
                                                         #]
list1=["even" if x%2==0 else "odd" for x in range(5)]   
list3=[1,2,3,4]
list4=[x+5 for x in list3]#creates a new list
print(list4)

#methods like count or anything

fruits=["apple","banana"]
new1=[num.count("a") for num in fruits]
print(new1)

#sets
