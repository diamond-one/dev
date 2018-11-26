#Important one start * for normal arguments, two stars ** for keyword arguments

#adding 5 arguments to print
print(1,2,3,4,5)

#This will print a list, because there is only one argument , a list.
numbers = [1,2,3,4,5]
print(numbers)

#The star here, unpacks the numbers list into individual items
print(*numbers)

#Unpacking also works on stings
string = "Unpack me"
print(*string)

def add (x,y):
    return x + y

print (add(10,10))

#Adding unpacked numbers into a tuple
def unpack (*numbers):
    total = 70
    #looping though the numbers variable and adding 4 to each
    for number in numbers:
            total = total + number
    return (total)

print (unpack(1,1,1,1,1,1))


#Packing
def about (name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)

#
dictionary = {"name" : "Matt", "age": 32, "likes" :"Python"}
about(**dictionary)


#Packing into a dictionary
def foo(**kwargs):
    #this creates a dictionary storying the items with key words
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))

foo(Sally = "female", Ziyad = "male")

# * Packs into tuples, or into argumetns if you use them in a fucntion
# ** Packs keyword arguments, into a dictionary   
