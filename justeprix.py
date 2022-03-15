from random import randint

def jeu(fin):

    n = int(input("Je pense à un nb\n"))

    a = 0
    while a =! n:
        a = int(input("Entrez un nb"))
        if a < n :
            tent += 1
            print("Le nombre est plus grand")
        if a > n:
            tent += 1
            print("Le nombre est plus petit")

def IA():
    n = int(input("Je pense à un nb\n"))

    a = 0
    while a =! n:
        a = randint(1, fin/2)
        if a < n :
            
            print("Le nombre est plus grand\n")
        if a > n:
            
            print("Le nombre est plus petit\n")