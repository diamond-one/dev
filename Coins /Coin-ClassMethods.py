import random

class Pound:

#Constructor method (self refere to the object created eg. coin1)
    def __inti__(self,rare = False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #in mm
        self.thickness = 3.15 #in mm
        self.heads = True


#######Deconstructor ( Deleting/distroying the object)
    def __del__(self):
        print("Coin Spent!")
####################



    #Methods of the class object
    #The first perameter in any class method has to be 'self' (or what ever you called it
    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice