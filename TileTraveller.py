position = 11
n = "(N)orth"
e = "(E)ast"
w = "(W)est"
s = "(S)outh"
while position != 31 :
    if position == 11:
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position += 1
        else:
            print("Not a valid direction!")

    elif position == 12:
        print("You can travel: {} or {} or {}.".format(n,e,s))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position += 1
        elif choice == "s":
            position -= 1
        elif choice == "e":
            position += 10
        else:
            print("Not a valid direction!")
    elif position == 13:
        print("You can travel: {} or {}.".format(e,s))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "s":
            position -= 1
        elif choice == "e":
            position += 10
        else:
            print("Not a valid direction!")

    elif position == 21:
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position += 1
        else:
            print("Not a valid direction!")

    elif position == 22:
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "w":
            position -= 10
        elif choice == "s":
            position += 1
        else:
            print("Not a valid direction!")

    elif position == 23:
        print("You can travel: {} or {}.".format(e,w))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "w":
            position -= 10
        elif choice == "e":
            position += 10
        else:
            print("Not a valid direction!")
    elif position == 33:
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "s":
            position -= 1
        elif choice == "w":
            position -= 10
        else:
            print("Not a valid direction!")

    elif position == 32:
        print("You can travel: {} or {}.".format(n,s))
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position += 1
        elif choice == "s":
            position -= 1
        else:
            print("Not a valid direction!")
print("Victory!")