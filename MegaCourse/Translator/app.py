import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def define (word):
    w = word.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        print ('''Did you mean '%s' instead?''' % get_close_matches(w, data.keys())[0])
        yes = input("yes / no :".lower())
        if yes == "yes":
            w = get_close_matches(w, data.keys())[0]
            return data[w]
        elif yes == "no":
            return "Sorry, try enter your word again."
        elif yes != "yes" "no":
            return "Try again"
    else:
        return "Didn't recognise word."

while True:
    word = input("Enter word: ").lower()
    output = (define(word))
    if type(output) == list:
        print(output[0])

