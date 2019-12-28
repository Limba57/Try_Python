import re

print("Notre superbe calculatrice")
print("Tape 'fin' pour sortir du programme")
print("Tapez c pour réinitialiser l'equation")

previous = 0
equation = ""
compute = True
run = True


def check_option(str):
    if str == "fin":
        return False
    else:
        return True


def check_compute(str):
    global previous
    global equation

    if str == "c":
        previous = 0
        equation = ""
        perform_math()
        return False
    else:
        return True


def perform_math():
    global run
    global previous
    global equation
    global compute

    if previous == 0:
        equation = input("Entre une equation: ")
    else:
        equation = str(previous)+input(previous)

    check = re.sub('[0-9A-Z,*]','',equation)
    compute = check_compute(check)
    run = check_option(check)

    if compute & run:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        previous = eval(equation)
        print("Resultat: ",previous)


while run:
    perform_math()
print("A plus!!")
