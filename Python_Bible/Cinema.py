films = {
    "Finding Dory": [3,1],
    "Wreck it Ralph":[13,7],
    "Tarzan": [18,12],
    }

print ("Now Showing : Finding Dory , Wreck it Ralph, Tarzan")

while True:

    choice = input("What movie would you like to see?").strip().title()

    if choice in films:
        age = int(input ("How old are you?").strip())

        #Check user age
        if age >= films [choice][0]:

            #Check enough seats

            num_seats = films [choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry we are sold out")

        else:
            print ("You are to young to watch this film")
    else:
        print("Sorry we don't have that film...")


