"""
    Dictionaries are datatypes of format key maps value. Similar to the gate and keys the in a dictionary to access any
    value we need to know the key to the particular value.

    The value stored in a dictionary may be anything an array, a tuple, a list, even a dictionary and any other
    datatype but the Key in a dictionary must be a string.

    it can be declared as,
    var = {}
    where var is an empty dictionary.

    Its characterstics are,
    1. It is mutable.
    2. It can be nested.
    3. Dictionary are dynamic datatype.
"""
var = {}
print(type(var))

"""
    Adding elements in a dictionary,
"""

var['dad'] = 'Head of family'
var['mom'] = 'Hardworking'
var['brother'] = 'Absolute fool'
var['me'] = 'Boring Fellow'


print(var)

"""
    Dictionary are mutable objects i.e. the value contained in a key can be changed based on the users need.
    Lets view an example as,
"""

var['me'] = 'Boring and an Idiot'
print(var)

if 'Boring and an Idiot' in var.values():
    print("Dictionary is Mutable")
else:
    print("Dictionary is not mutable.")


"""
    Dictionary as Dynamic data type 
"""
initial = len(var)
var['little_brother'] = 'Lovely'
final = len(var)
if initial-final is 0:
    print("Not Dynamic")
else:
    print("Dynamic")


# Dictionary Comprehension....

