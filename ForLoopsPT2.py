students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

for key in students.keys():
    for name in students[key]:
        if "z" in name:
          print(name)

#X is our variable,
even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)


#################

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
#w is our variable, it can be anything,
# but when we put after 'for' every item in our list (words) will become 'w' for the time being
#What we are doing is making every item the w variable, then making them all lowercase using the .lower()
#and upper case using the .upper() method. THEN we are getting the length of the original word in the list with the .len() method
answer = [[w.upper(),w.lower(), len(w)] for w in words]
print(answer)
