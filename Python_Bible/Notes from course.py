Udemy: Python
Bible

Useful
from Youtube:

# new line
print(“\n”)
# new lines
print(“\n” *5)



Section
3:

Variables
Little
boxes
that
store
stuff / values...data.Each
one
has
a
unique
name
so
we
can
identify
the
box.

It
has
a
name[case
sensitive] (the name of the box.And a value (what’s inside the box).
X = 1
    ..
    Each
variable
has
a
type /


class .
    To
    find
    out
    the
    type /

    class:

        >> > type()

>> > x = 1
>> > type(x)
<

class 'int'> INTERGER

>> > y = "this is a string"
>> > type(y)
<

class 'str'> STRING

>> > p = 4.332
>> > type(y)
<

class 'float'> FLOAT


Naming
techniques - keep
it
clear - start
them
with a letter

Camel
case: secondNumber
Another
type
of
camel
case: SecondNumber
With
underscores: second_number

Using
Variables:

first_number = 1 + 1
second_number = 10 + 10
total = first_number + second_number
print(total)

---------------------------
Section
4:

What
operators
are: a
symbol
that
let
us
to
a
task.Eg. + - * /.They
tell
python
what
to
do
Addition
Subtraction
*Multiplication
/ Division(this
will
always
create
a
float)
% Modulo - Finds
the
remainder
of
a
division
Eg.
10 % 2 = 0.
Ten is divided
by
2
5
times and there is no
remainder.Eg2.
15 % 4 = 3(15
divided
by
4, the
remainder is 3)
** to
the
power
of(squared)

Modulo
function

Float
Variable
type

Order
Python
Computes(order
of
computations)

BODMAS

B - Brackets
O - Order(squaring, cubing)
D - Division
M - Multiplication
A - Addition
S - Subtraction

---------------------------
Health
Potion.

# Health potion script
import random

health = 50
# could you make the difficulty an input from the shell?
difficulty = 3

health_potion = int(random.randint(25, 50) / difficulty)
health = health + health_potion

print(health)

Explained:
Imported ‘random’ This is a
python
standard
module
that
has
a
random
number
generator
-info
for this is in the python docs.

By
deviding
the
random
number
generated
we
created
a
float
variable.We
didn’t
want
this
so
we
used
somthing
called ‘casting’

int(random.randint(25, 50) / difficulty)

To
make
our
final
number
an
integer

_____________________
Section
4 - lecture
16

Using
some
of
the ‘math’ module

Forcing
a
round
down:
>> > import math
>> > math.floor(1.8)
1

Forcing
to
round
up:
>> > math.ceil(2.1)
3

Pi
>> > math.pi
3.141592653589793
>> >

__________________
Numbers
section
review

Basic
algebra
Mathmatical
operators
+- * % / **

interger
type
number(whole
number)
Float
type
number(number
with decimals)

Order
of
oppperations
BODMAS
Brackets, Orders
of
powers, Division, Multiplication, Addition, Subtraction
Importing
modules
Import
math

Casting
type:
>> > int(34.3)
>> > 34

_________________

Section
5

STRINGS - information
inside
quotation
marks “Hello
world”

>> > name = "Matt"
>> > print(type(name))
<

class 'str'>

>> > print("hello world")
hello
world

Using
different
types
of
quotes
means
that
you
can “quote” within
a
string.
eg:
>> > message = 'John said to me "I will see you later"'

Using
triple
quotes
boxes in a
broken
string
Eg:
>> > print("""Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.""")

Gathering
input:

Storing
input as a
varible
String
concatenation

String
formatting

Email
slicer

Fix
broken
strings

Writing
an
outline
for you code using comments
# Ask the user their name
# Ask user for their age
# Ask user for city
# Ask user what they enjoy


# Create output text
# Print output to screen

Hello
you
program
# Ask the user their name
name = input("What is your name: ")

# Ask user for their age
age = input("What is your age?: ")

# Ask user for city
city = input("What city do you live in?: ")

# Ask user what they enjoy
enjoy = input("What do you sport do you enjoy?: ")

# Create output text
string = "Cool, nice to meet you {}, {} ... the best age. {}sounds cool too,do you do {} there?"
output = string.format(name, age, city, enjoy)

# Print output to screen
print(output)

Formating
output = "Hello my names is {} and I am {} years old. I live in {} and I love Python".format(name, age, place)

_________________

Sting
tool
kit / String
Methods

>> > string.method()

>> > "hello".count("e")
1
# Counting things me
>> > text.count()

# making all upper case
>> > x = "happy birthday"
>> > x.upper()
'HAPPY BIRTHDAY'

# making all lower case
>> > x.lower()

# capitalizing text
>> > x = "hi"
>> > x = x.capitalize()
>> > print(x)
Hi

# is text only letters
x.isalpha()

# is text only numbers
x.isdigit()

# is text alphanumeric
x.isalnum

# Finding the index of something in a sting
>> > x = "hi"
>> > x.index("hi")
0

# finding something, that might not be there, this is a good way to look for something, but if the search fails you won’t get an error and your code will continue
x.find

# stripping things from strings
>> > y = "000000hi000000"
>> > y.strip("0")
'Hi'

# left strip
l.strip

# right strip
r.strip

# stripping spaces
# length of string
name = input(“what is your
name?: “).strip()
Matt
Diamond
len(name)

HELP > PYTHON
DOCS > PYTHON
STANDARD
LIBRARY > TEXT
SEQUENCE
TYPE > 4.7
.1
______________________

Slicing
strings

# Strings are :
Strings
are
iterable and unmutable.Meaning
every ‘element’ has
an ‘index’

Eg: “hhhhhhhhhh” string
would
have
the
indexes
of “01234567
8910”


eg.
Matthew
Diamond
>> > word[1]
'a'

# Taking a slice
variable[start:end:step / increment]

Eg
>> > word = "supercalifragilisticexpialidocious"
>> > word[5:9:1]
'cali'

# taking a slice from an index to the end, use [:] with nothing after it
>> > word[0:]

# taking everything up until an index . Leave the start blank
>> > word[:7]

# reverse the order of a string
>> > word[::-1]

# Slicing using computer to count the index
>> > word = "supercalifragilisticexpialidocious"
>> > word.index("cali")
5
>> > word = "antidisestablishmentarianism"
>> > answer = word[word.index("est"):word.index("ari")]
>> > print(answer)
establishment

__________________
EMAIL
SLICER

# Get the users email address
email = input("What is your email: ").strip()

# Slice out the user name
# slice is made by email[::]
# Then we are taking the slice by choosing an index which is done by email.index()
user = email[:email.index("@")]

# Slice out the domain name
domain = email[email.index("@") + 1:]

# format a message
# format can be added to the end of the string, because it's a string method
output = "The user name is {} and the domain name is {}".format(user, domain)

# Display message
print(output)

__________________

LOGIC

Boolean
Data
type
<

class 'bool'>


They
only
have
two
values, True or False.You
get
these
by
making
a
logical
comparison
between
two
pieces
of
data.

# They need capitals on ‘True’ and ‘False’ otherwise python sees it as a variable
B = True
C = False

Conditional
Operators
Greater
than <
Less
than >
Equal
to ==
Not
Equal !=
Greater
than or Equal
to >=
Less
than or Equal
to <=

If
statements / if - else statements
# What is an if statement
>> > if condition
    An if statement
    where if the
    condition is True, the
    program
    will
    continue

If
condition:
Code
elif condition
2:
Code
2
elif condition
3:
Code
3
else:
Code
4

num1 = 100
num2 = 50

if num1 > num2:
    print("Num1 is bigger than Num2")

# If the conditions are the same
num1 = 100
num2 = 100
if num1 > num2:
    print("Num1 is bigger than Num2")
elif num2 > num1:
    print("Num2 is bigger than Num1")
else:
    print("They are the same")

Logic
keywords

Logical
Operators - Combine and modify
conditions

# not : reverses what you would get otherwise


# ’not’ Logical operator


# this basically means false

>> > not True
False
>> > not False
True
>> > not 2 < 3
False

# ‘if not’
>> > x = 10
>> > y = 20
>> > if not y < x:
    print("it worked")
it
worked

AND
operator
# and : gives you True if A and B are BOTH True
# only gives you true if both inputs are true

>> > if c >= 10 and d > 1:
    print("it worked")
it
worked

NOT - AND

SECTIO
6
Lecture
32 - NEEDS
MORE
STUDY

_______
“Or” Logical
Operator
# gives us True if any of the conditions are true
# or : gives you True if either A or B is True


c = 5
b = 1
if c > 1 or b > 1:
    print("it worked")

# forcing to False answers twice, then getting the oppisite [the not] which would be True and give the print text
if not (c > 100 or b > 100):
    print("that worked too")

# all combined /more complex
c = 6
d = 2
if ((c > 5 and d > 5) or (c > 1 and d > 1)):
    print("it worked")

__________________
LISTS
# data kept in one box. []
# list elements are found using their index. Which start from 0
# list items are separated by a comma

# to find an item. Type the list name then the index you want in ‘[]’
>> > list_name = ["green", "blue", "yellow"]
>> > list_name[1]
'blue'

# slicing a list [start:end:step]
>> > list_name = ["green", "blue", "yellow"]
>> > list_name[1::]
['blue', 'yellow']

# lists inside lists
>> > list_name = ["green", ["purple", "orange"], "blue", "yellow"]
# the entire list inside a list counts as a single index of the first list:
>> > list_name[1]
['purple', 'orange']

# getting a single index from inside the second list
>> > list_name[1][0]
'purple'
>> >

# Adding to a list
list.append()
List = list + [a, b, c, d]
a = a + list(str(123)) - this
adds
123 as individual
strings
eg. ‘1’, ’2’, ’3’
a = a + [[5, 6, 7]] - this
will
add
5, 6, 7
list as a
list
inside
the
original
list
list.append([5, 6, 7]) - this
will
add
5, 6, 7
list as a
list
inside
the
original
list
list.insert(2, 100) - this
will
insert
100
at
index
2 in the
original
list
# insert slice
list.insert(2, [3, 4, 5]) - this
will
insert
the
new
list
at
index
2

_______________

Tuples
# A data type like a list which once created, cannot be changed (imutable)
our_tuple = 1, 2, 3, "1", "2", "3"
our_tuple = (1, 2, 3, "1", "2", "3")
# they can be sliced
our_tuple[0:3]
(1, 2, 3)
# Things can not be added to them

# Assigning multiple variables at once
(A, B, C) = 1, 2, 3
>> > A
1
>> > B
2
>> > C
3

D, E, F = [1, 2, 3]
>> > A
1
>> > B
2
>> > C
3

G, H, I = “789”
>> > G
‘7’
>> > H
‘8’
>> > I
‘9’


_______________

Dictionaries
# Items(students) keys(Alice) and values (25)
Students = {“Alice”:25, “Clair”:21, “Bob”:22}

# adding a new key to a existing value (fred to the age of 25)
Students[“Fred”] = 25

# deleting a key from
del students



