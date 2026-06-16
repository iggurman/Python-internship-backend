# Dictionary is a data type that is mutable and stores values in the form of
# key:value pairs.
# Dictionary is ordered (Python 3.7+).
# Keys are unique, but values can be duplicated.
# Uses {} and : to separate keys and values.
#also it replaced the value if the keys are duplicate

# keys: int, float, str, bool, tuple, frozenset
# values:

dict1 = {"id": 1, "name": "gurman", "age": 22}

print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

# Loop for accessing values
for value in dict1.values():
    print(value)

# Loop for accessing keys and values
student = {"maths": 98, "hindi": 67, "python": 95}

total_sum = 0

for key, value in student.items():
    print(key, ":", value)
    total_sum += value

print("Total =", total_sum)
print("Average =", total_sum / len(student))
print("----------------------")
# Nested Dictionary

students = {
    1: {"maths": 66,"python": 22,"english": 80},
    2: {"maths": 66,"python": 23,"english": 80},
    3: {"maths": 66,"python": 20,"english": 80},
    4: {"maths": 66,"python": 24,"english": 80},
}

for key in students.keys():
    print(key)
for value in students.items():
    print(value)
    
dict={1:{"m":20,"n":30},2:{"k":40,"g":50}}
print(dict.values())
print(dict[1]["m"])

