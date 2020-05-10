list1 = [2, 3, 4, 5, 6, 7]

# List Comprehension
"""
    No no condition: [<VariableToAdd> for-loop-defining-variable]
    Case of Single IF: [<VariableToAdd> for-loop-defining-variable <if condition>]
    Case of IF...Else: [<Value_for_true> if <condition> else <Value_for_false> for-loop-defining-variable]
"""
# Single Condition
list2 = [x for x in list1 if x % 2 == 0]
print(list2)

# if ...else List comprehension
list3 = [int(x/2) if x % 2 == 0 else x for x in list1]
print(list3)


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


# set comprehension
list_prime = set(no for no in list1 if is_prime(no))
print(list_prime)

print(["Even" if x % 2 == 0 else "Odd" for x in list1])
print([x**2 for x in range(2, 11)])

print({x: "Even" if x % 2 == 0 else "Odd" for x in list1})

list3 = [[1, 2], [3, 4]]

print([y for x in list3 for y in x])


abc = lambda x, y: (x - y) % y
print(abc(1,2))


def sum_nu(x,y):
    return x+y


# function assignment
sum_nums = sum_nu
print(sum_nums(1, 2))

b = lambda x, y: x + y
print(b(1, 2))

list5 = [1, 2, 3]
list6 = [4, 5, 6]
print(list(map(lambda x, y: x+y, list5, list6)))
print(list(map(b, list5, list6)))