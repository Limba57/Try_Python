
def my_function(str1,str2):
    print("This is my function")
    print("first parameter str1: "+str(str1))
    print("second parameter str2: "+str(str2))
    print("End of my function")
    print("-----")


def my_second_function(a: str, b: str):
    print("This is my second function")
    print("first parameter a: " + a)
    print("second parameter b: " + b)
    print("End of my function")
    print("-----")


def my_third_function(truc1, truc2):
    print("This is my third function")
    print("first parameter", truc1)
    print("second parameter", truc2)
    print("End of my fonction")
    print("-----")


def my_quatrieme_function(truc1="truc1", truc2="truc2"):
    print("c'est ma quatrieme fonction")
    print("premier parametre", truc1)
    print("deuxieme parametre", truc2)
    print("-----")


my_function("first", "second")

my_function(1, 2)

my_second_function("a", "b")

my_second_function(str(1), str(2))

my_third_function("truc 1", "truc 2")

my_third_function(1, True)

my_quatrieme_function()

my_quatrieme_function("premier parametre ?")

my_quatrieme_function(truc2="deuxieme parametre")

my_quatrieme_function(truc2="deuxieme parametre",truc1="premier parametre")





