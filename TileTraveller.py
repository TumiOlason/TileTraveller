#https://github.com/TumiOlason/TileTraveller
#

def position_changer(number,position,allowed):
    number = number.lower()
    if number == 'n' and allowed.find("n") != -1:
        position += 1
    elif number == 'e' and allowed.find("e") != -1:
        position += 10
    elif number == 's' and allowed.find("s") != -1:
        position -= 1
    elif number == 'w' and allowed.find("w") != -1:
        position -= 10
    else:
        print("Not a valid direction!")
        return position
    return position

def position_allowed(position):
    if position == 11:
        return "n"
    elif position == 12:
        return "ns"
    elif position == 13:
        return "es"
    elif position ==21:
        return "n"
    elif position == 22:
        return "sn"
    elif position ==23:
        return "ew"
    elif position==32:
        return "ns"
    elif position ==33:
        return "sw"
position = 11
n = "(N)orth"
e = "(E)ast"
w = "(W)est"
s = "(S)outh"


while position != 31 :
    if position == 11:
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        position = position_changer(choice,position,position_allowed(position))

    elif position == 12:
        print("You can travel: {} or {} or {}.".format(n,e,s))
        choice = input("Direction: ")
        position = position_changer(choice,position,position_allowed(position))

    elif position == 13:
        print("You can travel: {} or {}.".format(e,s))
        choice = input("Direction: ")
        position = position_changer(choice,position,position_allowed(position))

    elif position == 21:
        print("You can travel: {}.".format(n))
        choice = input("Direction: ")
        position = position_changer(choice,position,position_allowed(position))

    elif position == 22:
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")
        position = position_changer(choice,position,position_allowed(position))

    elif position == 23:
        print("You can travel: {} or {}.".format(e,w))
        choice = input("Direction: ")
        position = position_changer(choice,position,position_allowed(position))

    elif position == 33:
        print("You can travel: {} or {}.".format(s,w))
        choice = input("Direction: ")

        position = position_changer(choice,position,position_allowed(position))

    elif position == 32:
        print("You can travel: {} or {}.".format(n,s))
        choice = input("Direction: ")
        position = position_changer(choice,position,position_allowed(position))

print("Victory!")