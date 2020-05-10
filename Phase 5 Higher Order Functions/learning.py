"""
    Learning MAP, REDUCE, and FILTER as higher order functions.
"""
from functools import reduce


def is_prime(num):
    if num is 0 or num is 1:
        return True
    for each in range(2, int(num)):
        if num % each == 0:
            return False
    return True


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
list_2 = [1, 2, 3, 5, 7]
list_3 = [x for x in range(0, 100) if is_prime(x)]
print(list_3)

# Introduction to MAP Function
list_4 = list(map(is_prime, list_1))
print(list_4)

# Introduction to Filter..
def calcMean(args):
    sum = 0
    for each in args:
        sum += each
    return sum / len(arr)


arr = [1, 4, 5, 16, 18, 48, 34, 22, 15, 20]
mean = calcMean(arr)
list_5 = list(filter(lambda x: x > mean, arr))
print(list_5)


# Introduction to REDUCE
multiplier = lambda x, y: x + y
data = [2, 3, 5]
print(reduce(lambda x, y: x + y, data))

"""
    For reduce 
    0, 1 --> result(), 3 --> 
"""

