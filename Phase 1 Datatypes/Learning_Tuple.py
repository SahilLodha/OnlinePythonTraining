"""
    What is a Tuple in python?
    => Tuple is an iterable datatype which is mutable in nature. A tuple can be initialized as,
"""

tuple_example = ()
tuple_example_two = tuple()
print(type(tuple_example))
print(type(tuple_example_two))

"""
    Both the above mentioned ways are valid.
    
    The various properties of tuple are
    1. It's an indexed datatype.
    2. They are immutable.
    3. They can contain arbitrary datatype within itself.
    4. They can be nested. 
"""
# Example of Tuple containing arbitrary datatype.
tuple_example = ([1, 2, 3], {'a': 'Hello', 'b': "Hi", 'c': "Koniciwa"}, "Saying hello in different ways", 3)
print(tuple_example)

# Example for indexed tuple
print("\nIn tuple tuple_example: ")
for index, value in enumerate(tuple_example):
    print(index, " is position of ", value)

# Tuple is immutable.
# __add__() or similar functions are called magic functions in python.
tuple_example_two = tuple_example.__add__(('a', 'b', 'c'))

if tuple_example_two is tuple_example:
    print("Tuple is Mutable.")
else:
    print("Tuple is Immutable")

# Nested Tuple:
tuple_example = ()
tuple_example_two = tuple()

tuple_example = tuple(i**2 for i in range(1, 4))
print(tuple_example)
