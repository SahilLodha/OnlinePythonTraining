"""
    Lambda function is a feature of python which allows you to create anonymous function for use in the place it has
    been created. It is an inline anonymous function.
"""


def multiply(a, b):
    return a*b


# Use of lambda
# Example 1
# Creating other functions through lambda and a existing function
square_fun = lambda x: multiply(x, x)
cube_fun = lambda x: x*square_fun(x)
print(square_fun(2))
print(cube_fun(3))

# Example 2
# Need of anonymous function: Map, Reduce, Filter and many more
user_value = input("Enter What ever you like....")
vowels = ['a', 'e', 'i', 'o', 'u']
list_input = user_value.split(' ')




