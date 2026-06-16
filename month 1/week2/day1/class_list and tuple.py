# List can store same or different data types
# List is mutable (can be changed)

my_list = [12, "demo", 3.6, True]

my_list.insert(1, 16)      # Insert 16 at index 1
my_list.append(98)         # Add single value at end

list2 = [1, "hello", "yo", False]
my_list.extend(list2)      # Add multiple values

my_list.remove(True)       # Remove first occurrence of True

my_list.pop(3)             # Remove value at index 3
# If no index is given, removes last element

print(my_list.index("demo"))   # Find index of value
print(my_list.count(12))       # Count occurrences

# my_list.sort()               # Works only if elements are comparable

print(my_list)

my_list.clear()                # Empty the list
# Tuple is immutable (cannot be changed)

my_tuple = ("demo", 12, 55)

# Accessing values
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# Packing means storing multiple values in one tuple.
student = ("demo", 12, 55)

# Unpacking
student = ("demo", 12, 55)

name, age, weight = student

print(name)
print(age)
print(weight)