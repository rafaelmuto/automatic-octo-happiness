# LISTS: Lists are ordered collections of items that can be changed (mutable).

print('================\n','LISTS', '\n================')

a_list = [1,2,3,4,5,6,7,8,9,10]
b_list = ['a','b','c','d','e','f','g','h','i','j']

print(a_list)
print(b_list)


# Slicing the lists 
# slice(start, end, step)
sliced_a_list = a_list[2:5]
print(sliced_a_list)

sliced_b_list = b_list[2:10:2]
print(sliced_b_list)    

# cloning a list
cloned_a_list = a_list[:]
print(cloned_a_list)


# SETS: Sets are unordered collections of unique elements
# faster than lists

print('================\n','SETS', '\n================')

a_set = {1, 2, 3, 4, 5}
b_set = {'a', 'b', 'c', 'd', 'e'}

empty_set = set()
print(type(empty_set))


print(5 in a_set)  # Check if 5 is in a_set
print('a' not in b_set)  # Check if 'a' is in b_set



# DICTIONARIES: Dictionaries are collections of key-value pairs
print('================\n','DICTIONARIES', '\n================')

a_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

for key, value in a_dict.items():
    print(f"{key}: {value}")

print(a_dict.values())
print(a_dict.keys())


# TUPLES: Tuples are ordered collections of items that cannot be changed (immutable)
print('================\n','TUPLES', '\n================')

a_tuple = (1, 2, 3, 4, 5)
b_tuple = ('a', 'b', 'c', 'd', 'e')
empty_tyuple = tuple()

for item in a_tuple:
    print(item)

# list from tuple
tuple_to_list = list(a_tuple)
print(tuple_to_list)


# Enumerate: Returns an enumerate object, which is an iterable that contains pairs of index and value
print('================\n','ENUMERATE', '\n================')

for index, value in enumerate(b_tuple):
    print(f"Index: {index}, Value: {value}")


# List Comprehensions: A concise way to create lists
print('================\n','COMPREHENSIONS', '\n================')

squared_list = [x**2 for x in range(10)]
print(squared_list)
# Conditional List Comprehensions: Create a list with conditions
even_squared_list = [x**2 for x in range(10) if x % 2 == 0]
print(even_squared_list)
# Dictionary Comprehensions: A concise way to create dictionaries
squared_dict = {x: 2**x for x in range(20)}
print(squared_dict) 

square_list = [[x*y for x in range(10)] for y in range(5)]
print(square_list)

disible_for_list = [x for x in range(100) if x % 3 == 0]
print(disible_for_list)



# ARGS# *args and **kwargs are used to pass a variable number of arguments to a function
print('================\n','ARGS and KWARGS', '\n================')

def example_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
example_function(1, 2, 3, name='Alice', age=30)
# *args allows you to pass a variable number of positional arguments
# **kwargs allows you to pass a variable number of keyword arguments
# Using *args and **kwargs in a function
def add_numbers(*args):
    return sum(args)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Using *args and **kwargs
add_result = add_numbers(1, 2, 3, 4, 5)
print(f"Sum of numbers: {add_result}")
print_info(name='Alice', age=30, city='New York')

# Using *args and **kwargs in a class
class ExampleClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def display(self):
        print("Args:", self.args)
        print("Kwargs:", self.kwargs)


# TRY EXCEPT: Exception handling in Python
print('================\n','TRY EXCEPT', '\n================')
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Finally block will always execute
finally:
    print("This will always execute, regardless of whether an exception occurred or not.")

# Custom exception
class CustomError(Exception):
    """Custom exception class."""
    pass
try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(f"Custom Error: {e}")




# LAMBDA FUNCTIONS: Anonymous functions in Python
print('================\n','LAMBDA FUNCTIONS', '\n================')

# Lambda functions are small anonymous functions defined with the lambda keyword.
add = lambda x, y: x + y
multiply = lambda x, y: x * y

print(f"Add: {add(5, 3)}")  # Output: Add: 8
print(f"Multiply: {multiply(5, 3)}")  # Output: Multiply: 15

# Lambda functions can also be used with higher-order functions like map, filter, and reduce
# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared Numbers: {squared_numbers}")  # Output: Squared Numbers: [1, 4, 9, 16, 25]
# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even Numbers: {even_numbers}")  # Output: Even Numbers: [2, 4]
# Using lambda with reduce
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum of Numbers: {sum_of_numbers}")  # Output: Sum of Numbers: 15
# Using lambda with sorted
sorted_numbers = sorted(numbers, key=lambda x: -x)  # Sort in descending order
print(f"Sorted Numbers: {sorted_numbers}")  # Output: Sorted Numbers: [5, 4, 3, 2, 1]
# Using lambda with sorted
sorted_strings = sorted(b_list, key=lambda x: x.lower())  # Sort strings case-insensitively
print(f"Sorted Strings: {sorted_strings}")  # Output: Sorted Strings: ['a', 'b', 'c', 'd', 'e']
# Using lambda with sorted
sorted_tuples = sorted(zip(a_list, b_list), key=lambda x: x[0])  # Sort tuples by first element 
print(f"Sorted Tuples: {sorted_tuples}")  # Output: Sorted Tuples: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
