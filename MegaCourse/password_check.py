#While loop will run until a contion is True
correct_password = "1234"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password. Enter password: ")

#This is an example of string formating
message = "Hi %s %s Logged in" % (name, surname)
print(message)


#Date and time objects

import datetime
from datetime import datetime

delta = datetime.now() - datetime(1900, 12, 31)