from tkinter.constants import N
from fltk import *

lst = ["alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette"]

cree_fenetre(1000, 1000)
image(500, 200, 'paquet.png')
texte(75, 400, 'Jouer', couleur='Blue', taille=30)

"""
def jeu(nb_alum, retrait):
    
    Gagnant du jeu avec nombre donné d'alumette à retirer en fonction du nombre d'alumettes totales


    while len(lst) > retrait:
        for i in range(retrait):
            lst.pop(0)
    if len(lst) == retrait:
        print("joueur 1 à gagné")
    else:
        print("joueur 2 a gagné")
    
    if len(lst) == 0:
        for i in range(len(lst)):
            lst.pop(i)

    return lst
"""

def create_game(nb_alum):
    """
    >>> create_game(5)
    [alumette, alumette, alumette, alumette, alumette]
    """
    
    lst = []
    for i in range(nb_alum):
        
        lst.append("alumette")

    return lst
    

def retrait_alum(lst):
    """
    """

    if len(lst) > 0:
        lst.pop()

    return lst

def coup_possible(lst, k, coup, rang):
    """
    """
    return not coup <= len(lst[rang]) and not coup < k

def tour_par_tour():
    """
    """

    cmpt = 1

    if cmpt == 2:

        cmpt -= 1
    else:
        cmpt += 1
        
    return cmpt

def setting(n):
    """
    """
    nb_alum = [n]
    type_game = ["Mode misère", "Mode Normal"]
    couleur_interface = ['Blue', 'Black', 'Red']

    return n

def QuitGame():
    """
    """
    exit()

def zone_clic(bouton1, bouton2, bouton3, clic):
    """
    """
    if bouton1 == clic:
        return create_game(setting())
    if bouton2 == clic:
        return setting()
    if bouton3 == clic:
        return QuitGame()




if __name__ == "__main__":
    ev = donne_ev()
    tev = type_ev(ev)

    







