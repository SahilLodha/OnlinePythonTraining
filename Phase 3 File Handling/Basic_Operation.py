myfile = open('fruits.txt', 'r')
content = myfile.read()
myfile.close()

"""
    with is also called context manager,
    It helps by automatically closing the file opened once the scope of file object is
    breached.
"""
with open('fruits.txt', 'r') as myfile:
    content = myfile.read()

print(content)

"""
    To access the lorem the txt the argument of the open function must be chained.
    open(location, open method)
    Writing Methods
    Basic 3:
    1. Write, w
    2. Append, a
    3. Read (Default), r
    4. Create New File, x
    Augmented Writing Methods:
    1. read and write, w+
    2. read and append, a+

"""

with open('files/lorem.txt') as f:
    print(f.read())


with open('fruits.txt', 'w') as f:
    f.writelines("Apple\nBannana\nCherries\nChiku\nPomogrenade\nAnd so on")

with open('fruits.txt', 'a') as f:
    f.writelines(['hello', 'appending into files'])


"""
    Copying contents of one file to another...
"""
with open('fruits.txt', 'r') as file_1:
    with open('copyfile.txt', 'w') as file_2:
        file_2.write(file_1.read())


with open("copyfile.txt", 'r') as f:
    print(f.read())

"""
    Example of w+
"""

with open('copyfile.txt', 'a+') as f:
    content = f.read()
    list_content = content.split("\n")
    if 'coco' not in list_content:
        f.write('\ncoco')

