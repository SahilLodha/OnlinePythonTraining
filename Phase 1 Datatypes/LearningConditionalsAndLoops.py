# Conditionals
"""
    They are of two types:
    1. if..else..
    2. if..elif..else..

    Syntax:
    if <condition1>:
        <Statements>
    elif <condition2>:
        <Statements>
    else:
        <Statements>
"""

string = "Sahil"
if 'an' in string:
    print('a Found')
else:
    print("A not found")


list1 = [0, 1, 2, 3, 4, 5]

if 0 in list1:
    print("0 is found")
elif 1 in list1:
    print("1 Found")
else:
    print('Not Found!')


#  Learning For Loop
"""
for <variable> in <iterable>
    <statements>
"""
marks = (89, 52, 70, 50)
sum = 0

for mark in marks:
    if mark < 40:
        print("Failed")
        sum = 0
        break
    else:
        sum += mark

if sum is not 0:
    print("Student Passed, Average: {:.2f}.".format(sum/len(marks)))