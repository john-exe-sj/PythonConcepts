
"""
Lists:
A list is a collection of items that can be of different types and is mutable, 
meaning you can change its elements after creation.
"""
# Example of a list
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Access an element by index
print("Element at index 2:", my_list[2])

# Modify an element
my_list[0] = 10
print("Modified list:", my_list)

# Add an element to the list
my_list.append(6)
print("List after appending:", my_list)

# Remove an element from the list
my_list.remove(3)
print("List after removing element 3:", my_list)

# Inserts an element to the list, given an index.
my_list.insert(1, 53)
print("List after inserting element 53 on index 1", my_list)

"""
Tuples:
A tuple is similar to a list but is immutable, meaning you cannot change its elements after creation.
"""

# Example of a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Access an element by index
print("Element at index 2:", my_tuple[2])

# Cannot modify a tuple (will raise an error)
# my_tuple[0] = 10

"""
Dictionaries:
A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
"""

# Example of a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary:", my_dict)

# Access a value by key
print("Age:", my_dict['age'])

# Modify a value
my_dict['age'] = 35
print("Modified dictionary:", my_dict)

# Add a new key-value pair
my_dict['gender'] = 'Female'
print("Dictionary after adding gender:", my_dict)

# Remove a key-value pair
del my_dict['city']
print("Dictionary after removing city:", my_dict)

# You can also loop through these structures as well: 

# LISTS
my_list = [1, 2, 3, 4, 5]

# Using a for loop
print("Looping through a list:")
for item in my_list:
    print(item)

# Using list comprehension
print("Using list comprehension:")
squared_list = [x**2 for x in my_list]
print(squared_list)

# TUPLES
my_tuple = (1, 2, 3, 4, 5)

# Using a for loop
print("Looping through a tuple:")
for item in my_tuple:
    print(item)

# Using tuple unpacking
print("Using tuple unpacking:")
for i, item in enumerate(my_tuple):
    print(f"Index {i}: {item}")

# DICTIONARIES

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using a for loop with keys
print("Looping through a dictionary (keys):")
for key in my_dict:
    print(key, ":", my_dict[key])

# Using items() method to iterate over key-value pairs
print("Using items() method:")
for key, value in my_dict.items():
    print(key, ":", value)

# Using dictionary comprehension
print("Using dictionary comprehension:")
squared_values = {key: value**2 for key, value in my_dict.items() if isinstance(value, int)}
print(squared_values)
