#Automating the printing of 1-10
num = 0

while num <= 10:
    print (num)
    num = num + 1

print (num)

#Automating the printing of 1-100, but only even numbers
num = 0

while num <= 10:
    if num % 2 == 0:
        print (num)
    num = num + 1

print (num)

#Asking user for names, with maxiumum of three names

l= []

while len (l) < 3:
    new_name = input ("Please add a new name: ").strip().capitalize()
    l.append(new_name)
print ("Sorry list is full")

