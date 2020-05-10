import json
import time
from difflib import get_close_matches


data = json.load(open('data.json'))


def search(w):
    word = w.lower()
    if word in data.keys():
        return True
    else:
        return False


def display(word):
    word = word.lower()
    if search(word):
        print(f"The meaning of {word}:\n{data[word]}")
        print("Similar words are", get_close_matches(word, data.keys()))
        time.sleep(2)
    else:
        suggestions = get_close_matches(word, list(data.keys()), cutoff=0.8)
        if len(suggestions) is 0:
            print("The input word cannot be found!")
            time.sleep(2)
        else:
            print("May be you have mistyped!\nSuggestions are:")
            for index, each in enumerate(suggestions):
                print(f"{suggestions[index]} to search Enter {index+1}")
            print("To exit Enter 0.")
            press = int(input("Enter a number: "))
            time.sleep(2)
            if press in range(1, 4):
                display(suggestions[press-1])
            elif press is 0:
                print("Have a great time")
            else:
                print("Wrong Number Entered!")


while True:
    word = input("Enter a Word: ")
    display(word)
    flag = input("Enter 'T' to continue and 'F' to Quit: ")
    if flag.lower() is 't':
        break
    else:
        continue



