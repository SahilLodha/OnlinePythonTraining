"""
    Methodology,
    1. We read file and get individual lines.
    2. We split each lines to with reference of space character to gain each word.
    3. We deal with words that contain '.' and ',' character at its end.
    4. We finally start to count the occurrences of each of these word. ( 2 ways to implement )
"""


def filterWordLast(word):
    if len(word) is not 0:
        if ord(word[-1]) in range(97, 123):
            return word
        elif ord(word[-1]) in range(48, 58):
            return word
        else:
            return word[0:len(word)-1]
    else:
        return word


def filterWordFirst(word):
    if len(word) is not 0:
        if ord(word[0]) in range(97, 123):
            return word
        elif ord(word[0]) in range(48, 58):
            return word
        else:
            return word[1:len(word)]
    else:
        return word


with open('files/lorem.txt', 'r') as f:
    content = f.read()
    list_lines = content.split('\n')
    """
        You can use readline if you want to.
    """

words = []

for each in list_lines:
    word = each.split(' ')
    words.extend(word)

words_case = [each.lower() for each in words]

"""
    applying filters:
    Opening and ending characters expect num and alphabets are removed.
"""
filtered_word = []
final_filter = []


for each in words_case:
    return_val = filterWordLast(each)
    filtered_word.append(return_val)

for each in filtered_word:
    final_filter.append(filterWordFirst(each))

"""
    Now Counting Words...
"""
count_dict = {}
for each in final_filter:
    if each in count_dict.keys():
        count_dict[each] += 1
    else:
        count_dict[each] = 1

print(count_dict)

