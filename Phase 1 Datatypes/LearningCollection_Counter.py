from collections import Counter

cnt = Counter()

# Opening a file and reading a single line
fileObj = open('LoremIpsum.txt', 'r')
content = fileObj.readline()
fileObj.close()

for each in content.split(" "):
    cnt[each] += 1

print(cnt)

# In short using the Counter object we can attain the same results as shown below
print(Counter(content.split(" ")))

"""
A Counter object syntax:
Counter(iterables | keywords args | string)
Note that for an string the words counts are returned along with a space character count if present
"""

# for an object that doesn't exist in the counter returns a 0 as shown below....
print("The count of a non-existing element is", Counter(content.split(" "))["sahil"])

"""
This indicates that setting an elements count to 0 is same as deleting it from the object.
i.e CounterObjName[<Element>] = 0 is same as del CounterObjName[<element>]

Now lets use this to read a file with multiple lines and count its contents..
The function wordClear() will clean all the words i.e. removing commas, brackets and fullstops from the word before 
counting..

Also an example of recursive function...
"""
cnt = Counter()


def wordClear(word):
    if word[-1] == ')' or word[-1] == '.' or word[-1] == ',' or word[-1] == '}' or word[-1] == ']':
        word = word[0:-1]
        wordClear(word)
    if word[0] == '(' or word[0] == '.' or word[0] == '{' or word[0] == '[' or word[0] == ',':
        word = word[1:]
        wordClear(word)
    return word


with open('LoremIpsum.txt', 'r') as f:
    content = f.read()

for line in content.split('\n'):
    for word in line.split(" "):
        word = wordClear(word)
        cnt[word] += 1

print(cnt)