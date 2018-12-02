from random import choice

questions = ["Where do babies come from?: ", "Why does water come out my pee pee: ", "Why do I have two daddys?: "]

question = choice(questions)
answer = input(question).lower().strip()

while answer != "just because":
    answer = input("Why").strip().lower()

#Trying to make it start again, so far it isn't working
print (input(question).lower().strip())

