def position_changer(number,position):
    number = number.lower()

    if number == 'n':
        position += 1
    elif number == 'e':
        position += 10
    elif number == 's':
        position -= 1
    elif number == 'w':
        position -= 10
    else:
        print("Not a valid direction!")
        return position
    
    return position



position = 11
n = "(N)orth"
e = "(E)ast"
w = "(W)est"
s = "(S)outh"


while position != 31 :
    if position == 11:
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        position = position_changer(choice,position)

    elif position == 12:
        print("You can travel: {} or {} or {}.".format(n,e,s))
        choice = input("Direction: ")
        position = position_changer(choice,position)

    elif position == 13:
        print("You can travel: {} or {}.".format(e,s))
        choice = input("Direction: ")
        position = position_changer(choice,position)

    elif position == 21:
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        position = position_changer(choice,position)

    elif position == 22:
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")
        position = position_changer(choice,position)

    elif position == 23:
        print("You can travel: {} or {}.".format(e,w))
        choice = input("Direction: ")
        position = position_changer(choice,position)

    elif position == 33:
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")

        position = position_changer(choice,position)

    elif position == 32:
        print("You can travel: {} or {}.".format(n,s))
        choice = input("Direction: ")
        position = position_changer(choice,position)

print("Victory!")