#Things can only be seen within thier scope
#This Variable is global.
a = 200
c = [1,2,3]

def f1():
    #this variable is local but also using the global
    # functions become little bubbles of code, working with themselves
    b = a + 10
    print(b)

def f2():
    a =  50
    print(a)
          #after the function is run, the variable disapears.

#Here we are changing the global varible 'a' by using the 'global' statement
def f3():
    global a
    a = 10
    print(a)
          #after the function is run, the variable disapears.

#Changing parts of a global list/dictonary
def f4():
    c[0] = 5
    print(c)

f1()
f2()
f3()
f4()
print(a)