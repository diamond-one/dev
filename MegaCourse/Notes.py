#Python is made of Variables / Objects and Functions on those

#All functions
>>>dir(__builtins__)

#int Fuction turns the input(argument) into an interger
int()

#float Function turns input(argument) into a float
float()

#str Function turns input(argument) into a string
str()

#All Methods
dir(__address__)

#All list methods
dir(list)

#methods are Object.Method(argument)

#HELP - this function gives you info on  methods
help(list.remove)

#Removeing from a dictionary
>>> person97.pop("name")
'Jack'
>>> person97
{'surname': 'Smith', 'age': '29'}

#Adding to a dictionary
>>> person97["name"] = "Jack"
>>> person97
{'surname': 'Smith', 'age': '29', 'name': 'Jack'}

#Changing an existing value
>>> person97["age"] = 30
>>> person97
{'surname': 'Smith', 'age': 30, 'name': 'Jack'}

#Mapping two lists to a dictionary:
>>> keys = ["a", "b", "c"]
>>> values = [1, 2, 3]
>>> mydict = dict(zip(keys, values))
>>> mydict
{'a': 1, 'b': 2, 'c': 3}


#Fucntions  (alsways starts with 'def')
def calculate_age(year):
        age = 2018 - year
        return age

calculate_age(1986)
32

#opening files
myfile = open("sample.txt")
content = myfile.read()
#Closing helps save memory space
myfile.close()
print(content)

#Reading text files
myfile.read()
#After reading a file, the curser is at the end of the file, so you need to return it
myfile.seek(0)

myfile = open("home/myfiles/sample.txt")

#Splint lines/text files into lists
fruits = fruits.splitlines()

file = open("fruits.txt", "r")
content = file.read()
file.close()
print(content)

#For loop
mylist = [1, 2, 3, 4, 5]
for self in mylist:
    print(self)

#For loop
mylist = [1, 2, 3, 4, 5]
for self in mylist:
    if self > 2:
        print(self)

#Reading and converting text into numbers
One way to do this is to use the read()  method:

myfile = open("fruits.txt")
content = myfile.read()
myfile.close()
content = content.splitlines()
for i in content:
     print(len(i))

Another way is to use readlines() :

file = open("fruits.txt")
content = file.readlines()
content = [line.strip() for line in content]
file.close()
for i in content:
    print(len(i))

#for loop
def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temp = [10, -20, 100]
for self in temp:
    temp = cel_to_fahr(self)
    print(temp)

#Creating and writing to a file
my_file = open("creating_file.txt", "w") #w mode is 'write'
my_file.write("Mike\nJoe\nJack")
my_file.close() #Close saves

#Appending text to file
my_file = open("creating_file.txt", "a") #a mode is 'append'
my_file.write("\nJane")
my_file.close() #Close saves

#Reading and appending text to file
my_file = open("creating_file.txt", "a+") #a+ mode is 'append'
my_file.read()
my_file.seek(0) () #puts curser at the start of the text file

#While loop will run until a contion is True
correct_password = "1234"
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password. Enter password: ")

print("Logged in")

#Date time moodule
from datetime import datetime
delta = datetime.now() - datetime(1900, 12, 12)
print(delta)

#String Formating a time to use with datetime module
then = datetime.strptime("2018-12-31", "%Y-%M-%D")
#Diffent format
then = datetime.strptime("2018:12:31", "%Y:%M:%D")

#Many more formats and usages here : http://strftime.org/

#Creating an output and printing it to a file
temperatures = [10, -20, -289, 100]
def writer(temperatures):
    with open("creating_file.txt", "w") as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n")
# Here we're calling the function, otherwise no output will be generated
writer(temperatures)

#Handleing Errors
try:
    a/b
except: