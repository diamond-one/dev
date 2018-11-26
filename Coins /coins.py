#Class names needs a capital
class Pound:

    value = 1.00
    colour = "gold"
    num_edges = 1
    diameter = 22.5 #in mm
    thickness = 3.15 #in mm
    heads = True

#creating the first instance
coin1 = Pound()
coin1.colour = "greenish"

coin2 = Pound()

#Demonstraing that each object has it's own characteristics, they are individual
print (coin1.colour)
print (coin2.colour)a


