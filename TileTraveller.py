#https://github.com/TumiOlason/TileTraveller
#we intend on using atleast two different functions to see if the step we want to take is allowed and then go those steps
#We then will be using if statements for each position of the 3x3 grid.

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
        return "nse"
    elif position == 13:
        return "es"
    elif position ==21:
        return "n"
    elif position == 22:
        return "sw"
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

    elif position == 12:
        print("You can travel: {} or {} or {}.".format(n,e,s))

    elif position == 13:
        print("You can travel: {} or {}.".format(e,s))

    elif position == 21:
        print("You can travel: {}.".format(n))

    elif position == 22:
        print("You can travel: {} or {}.".format(s,w))

    elif position == 23:
        print("You can travel: {} or {}.".format(e,w))

    elif position == 33:
        print("You can travel: {} or {}.".format(s,w))

    elif position == 32:
        print("You can travel: {} or {}.".format(n,s))

    choice = input("Direction: ")
    position = position_changer(choice, position, position_allowed(position))
print("Victory!")