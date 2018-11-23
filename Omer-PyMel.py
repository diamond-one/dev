#Importing Pymel
import pymel.core as pm

#Listing objects in the scene, in this case we chose to list cameras
pm.ls(type='camera')

#Creating test list, that is a list of what ever is selected
#Then selecting the first thing in the list [0] and getting it's 'shape'
#The shape of an object is the lowest layer in the hirachy of the objects. Lower than the Transform layer.
test = pm.selected()[0].getShape()
test[0]

#Creating a variable called 'obj' (could be called anything) that becomes the variable name for all items in selected
for obj in pm.selected():
    #Creating a string with format holes
    #The format holes are filled with first the obj name, then the translate Y value
    print('{} Y value is: {}'.format(obj, (pm.getAttr(obj + '.translateY'))))
    #same again but for the X value
    print('{} X value is: {}'.format(obj, (pm.getAttr(obj + '.translateX'))))
    #adding an empty line between printed info
    print
    ''
#creating a variable of the X value so that in can be added to the next line of code
value = pm.getAttr(test[0] + '.translateX')

#Making test list a string, then selecting object 0 and translateX then Value + 60 - Value from X
pm.setAttr(str(test[0]) + '.translateX', -(value + 60))

pm.selected()[0].getShape()