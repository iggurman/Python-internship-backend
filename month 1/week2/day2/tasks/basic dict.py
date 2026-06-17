dict={
    "name":"gurman",
    "age":22,
    "course":"mca"
}
print(dict["age"]) # give error if not found
print(dict.get("age")) #prints none if not found

dict["gender"]="male","female"
print(dict) #updating values
del dict["age"] #deletes key:value

# methods to access
print(dict.keys())
print(dict.values())
print(dict.items())

# get()
dict.get("name")
dict.update({"gender":"man"})
print(dict)

#looping through keys
for key in dict:
    print(key)
#looping through keys explicitly
for key in dict.keys():
    print(key)
#looping through values
for value in dict.values():
    print(value)
#for both key value pair
for key,value in dict.items():
    print(key,"-",value)

#nested dictionary
students = {
    "student1": {"name": "Gurman","age": 25},

    "student2": {"name": "John","age": 25}
}
print(students["student2"]["age"])#but it will print either name or age not both
