import re

print("Notre superbe calculatrice")
print("Tape 'fin' pour sortir du programme")

previous = 0
run = True


def check_quit(str):
    if str == "fin":
        return False
    else:
        return True


def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Entre une equation: ")
    else:
        equation = str(previous)+input(previous)

    check = re.sub('[0-9A-Z,*]','',equation)
    run = check_quit(check)

    if run:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        previous = eval(equation)
        print("Resultat: ",previous)


while run:
    perform_math()
