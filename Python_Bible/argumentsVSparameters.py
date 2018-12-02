def about (name, age, likes):
    sentences = "meet {}, They are {} years old and they like {}".format(name, age, likes)
    return sentences

#positional argument .. these need to be in the correct order
print (about("Jack", 23, "Python"))
#or, keyword argement, they can be in any order
print (about(age = 23, name = "Jack", likes = "Python"))
#The differnece, is the first is parameter based and the second is keyword based

#having a default value (the default value NEEDS to go last.
def about (name, age, likes = "Football"):
    sentences = "meet {}, They are {} years old and they like {}".format(name, age, likes)
    return sentences

print (about("Jack", 23,))
#the default perameter can be overwritten:
print (about("Jack", 23, "Python"))