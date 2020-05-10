"""
    String are any thing that are written within a single or a double quote in python.
"""
var_first = "Sahil"
var_last = 'Lodha'

print(type(var_first))
print(type(var_last))


# Example for multiline string
characterstics = """
The string is simply displayed as written.
    Some of the major characterstics of the string datatype are as follows:
    1. They are iterable.
    2. They are non-mutable or immutable.
    3. You are allowed to have multiline string using the triple quote.
    4. Special string also called Escape characters Exist.
"""


var = """Hello I am Sahil.
This is a Multiline String.
Look at the output of print(var) to understand Multiline String and ordinary String.
"""

print("Result of print(var): ", var)
print(characterstics)


# The string is a iterable datatype.
print("Example for iterable.")
for index, letter in enumerate(var_first):
    print(index, " Maps ", letter)

# String are immutable
"""
    String doesn't allow to change any specific value contained in it.
    for example,
    var[0] is S in the above program but if we right it as var[0] = 't'
    this is not allowed hence immutable.
"""