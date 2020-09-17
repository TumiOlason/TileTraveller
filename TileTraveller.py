position = "1,1"
n = "(N)orth"
e = "(E)ast"
w = "(W)est"
s = "(S)outh"
while position != "3,1":
    if position == "1,1":
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position = "1,2"
        else:
            print("Not a valid direction!")

    elif position == "1,2":
        print("You can travel: {} or {} or {}.".format(n,e,s))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position = "1,3"
        elif choice == "s":
            position = "1,1"
        elif choice == "e":
            position = "2,2"
        else:
            print("Not a valid direction!")
    elif position == "1,3":
        print("You can travel: {} or {}.".format(e,s))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "s":
            position = "1,2"
        elif choice == "e":
            position = "2,3"
        else:
            print("Not a valid direction!")

    elif position == "2,1":
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position = "2,2"
        else:
            print("Not a valid direction!")

    elif position == "2,2":
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "w":
            position = "1,2"
        elif choice == "s":
            position = "2,1"
        else:
            print("Not a valid direction!")

    elif position == "2,3":
        print("You can travel: {} or {}.".format(e,w))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "w":
            position = "1,3"
        elif choice == "e":
            position = "3,3"
        else:
            print("Not a valid direction!")
    elif position == "3,3":
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "s":
            position = "3,2"
        elif choice == "w":
            position = "2,3"
        else:
            print("Not a valid direction!")

    elif position == "3,2":
        print("You can travel: {} or {}.".format(n,s))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position = "3,3"
        elif choice == "s":
            position = "3,1"
        else:
            print("Not a valid direction!")
print("Victory!")