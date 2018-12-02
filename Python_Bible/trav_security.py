known_users = ["John","Matt", "Balu", "King Kong", "Fred"]

while True:
    print("Hi, My name is travis")
    name = input ("what is your name?: ").strip().capitalize()

    if name in known_users:
        print ("Hello{}!".format(name))
        remove = input ("Would you like to be removed from the system (y/n)?: ").lower()

        if remove == "y":
            print (known_users)
            known_users.remove(name)
            print(known_users)

    else:
        print("name NOT recognised")
