known_users = ["J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J",
               "J", "J", "J", "J", "J", "J",
               "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J",
               "J", "J", "J", "J", "J", "J",
               "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J",
               "J", "J", "J", "J", "J", "J", ]
x = len(known_users)

while True:
    print("Welcome to the VIP rub a dub bruv, strickly guestlist innit. I'm your bouncer Trav, We have", (x),
          "people inside 'avin it large.")
    name = input("You on the list blad? what's your name? : ").strip().capitalize()
    print("\n")

    if name in known_users:
        print("Aight {}!".format(name), "get in there, lets hale and hearty!")
        remove = input("Do you want me to cross you off the list, (yea/nah): ").lower()
        print("\n")

        if remove == "yea":
            known_users.remove(name)
            print("\n")

        else:
            print("I think you stuttered mate, I couldn't understand ya")
            print("\n")

    else:
        print("You're having a giraffe mate, you ain't on the list, on ya bike")
        add_me = input(
            "Giz us a fiver and I'll add you and your muffin' topping tart to the list? yea/nah ").strip().lower()
        print("\n")

        if add_me == "yea":
            known_users.append(name)
            print("Aight {}!".format(name), "get in there, lets hale and hearty!")
            print("\n")
        elif add_me == "nah":
            print("Well la de da, ya fucking creep, to good for the rub adub eh'")
            print("\n")


        else:
            print("I think you stuttered mate, I couldn't understand ya")
            print("\n")
