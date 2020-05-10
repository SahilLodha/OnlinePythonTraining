"""
    A function is a piece of code which performs a certain operation based on the code and the arguements passed in it.
    Futhermore, A function makes a program much more readable and Short.
"""

# Built in Functions
# These are predefined function that perform a certain task based on the operand passed, example,
a = 5
print('a')
print(a)

"""
    one of the most basically used function is print(). If a string is passed it simply outputs the string same for a number.
    in case of a variable it prints the value of the variable.

    It takes argument like variable name, string, integer, end character in a predefined format as,
    print(variable/string/integer, end=escape character)
    example,
"""

print("string", end='\t')   # \t == Tab Escape Character
print("tabbed value")
"""
    The default argument for end is "\n" also called newline character.
"""


# User Defined Functions
"""
    In cases where the user writes repeated codes in many places the user may create a function to perform such an operation.
    It can be done in python by using the def keyword which helps in creating a function.

    A function consist of two parts in python,
    1. Function Defination
    2. Function Call
    Example,
"""


# This is function Definition
def OddEven(x):
    if type(x) is int:
        if x % 2 == 0:
            return "Even"
        else:
            return "Odd"
    elif type(x) is dict:
        return "Cannot work on dict."
    else:
        result = []
        for each in x:
            if each % 2 == 0:
                result.append("Even")
            else:
                result.append("Odd")
        return result


# These are function call
print(OddEven((1, 2, 3)))
print(OddEven(1))
print(OddEven({'1': 5}))


# Infinite argument functions can be formed by args and kwargs.
def sumNum(*args):
    # sum = 0
    # for each in args:
    #     sum += each
    # return sum
    return sum([i for i in args])


print(sumNum(1, 2, 3, 4, 5))


def sumNumDict(**nums):
    return sum([nums[each] for each in nums.keys()])


print(sumNumDict(one=1, two=2, three=3, four=4))

"""
    factorial function
"""


def factorial(num):
    if num is 0:
        return 1
    else:
        prod = 1
        num_list = [i for i in range(1, num+1)]
        for each in num_list:
            prod *= each
        return prod


print(factorial(4))