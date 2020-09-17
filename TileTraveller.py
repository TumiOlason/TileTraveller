position = "1,1"
while position != "3,1":
    if position == "1,1":
        print("You can travel: (N)orth")
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position = "1,2"
        else:
            print("Not a valid direction!")
    if position == "1,2":
        print("You can travel: (N)orth")
        choice = input("Direction: ")
        choice = choice.lower()
        if choice == "n":
            position = "1,2"
        else:
            print("Not a valid direction!")