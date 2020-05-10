"""
    There are various datatype in python we discuss about the 4 major distinct type of data types along with there
    properties as:
    1. List
    => List is a iterative datatype which is declared as:
"""

var = list()
var_two = []
print(type(var))
print(type(var_two))

"""
    which shows that both are valid ways of declaring a list variable which initially stores no data.
    
    The list being a datatype follows some certain Characteristics. The characteristics of list are provided below:
    1. It is a mutable type of data type i.e. its value can be updated.
    2. They can Contain arbitrary objects.
    3. They are dynamic in nature. There size can be incremented as per need.
    4. They are indexed in nature.  
    5. They can be nested.
"""

for each in range(0, 20):
    if each % 2 == 0:
        var.append(each)

"""
    Same can be done as follow.
"""

var_two = [x % 2 == 0 for x in range(0, 20)]
print('var_two = ', var_two)
print('var = ', var)

"""
    This is called list comprehension which follows the structure:
    list_datatype = [{value} {value_definition} {condition}] in case of if only list comprehension else
    list_variable = ['value 1' if <condition> else 'value 2' {value_definition}]
"""

# Example for iterable and arbitrary object
index_data = []
for index, data in enumerate(var_two):
    index_data.append((index, data))
print(index_data)

"""
    Program code for the illustration of dynamic nature.
    A Data type is called Dynamic if its size grows with the increase in number of data.
    A Data type is called Mutable if it allows to change the values contained in it.
"""

initial_length = len(var)
var.append(20)
var.append(22)
final_length = len(var)

if final_length - initial_length is not 0:
    print('List is dynamic in Nature.')
else:
    print('List is not Dynamic in nature.')

if 20 in var:
    print("List is Mutable in nature.")
else:
    print("List is immutable in nature.")

"""
    Demonstration of Nested Lists.
    The list below contains lists of powers of 1, 2, 3 
    the first list contains 1,2,3 raised to a power of 1 the second list contains 1, 2, 3 raised to power to and 
    finally the third list contains 1, 2, 3 raised to power of 3.
"""

power_list = list()
for i in range(1, 4, 1):
    temp = []
    for j in range(1, 4, 1):
        temp.append(j**i)
    power_list.append(temp)

print(power_list)


"""
    More on list comprehension...
    1. Basic List Comprehension,
    2. If block List Comprehension,
    3. If....else block List Comprehension.
"""

# Basic
list1 = [i for i in range(1, 20)]
print(list1)

# if conditioned
list2 = [i for i in list1 if i % 2 == 0]
print(list2)

# If and Else both
list3 = ['odd' if x % 2 is not 0 else False for x in list1]
print(list3)