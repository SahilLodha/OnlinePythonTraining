from collections import OrderedDict

# Creating an general dictionary as
fruits = {
    'bananas': 4,
    'apples': 10,
    'mangoes': 45
}

test1 = sorted(fruits.items(), key=lambda t:t[0])
test2 = OrderedDict(sorted(fruits.items(), key=lambda t:t[0]))

print(test1)
print(test2)

test1.append(('carrots', 32))
test2["carrots"] = 32

print(test1)
print(test2)

# Sorting a dictionary based on value
print(OrderedDict(sorted(fruits.items(), key=lambda t:t[1])))