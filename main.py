from tkinter.constants import N
from fltk import *

lst = ["alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette"]



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

def zone_clic(bouton1, bouton2, bouton3, text):
    """
    """

    
    a, b = taille_texte(text)
    a1, b1 = bouton1
    a2, b2 = bouton2
    a3, b3 = bouton3
    print(ordonnee_souris())
    print(a1)
    if (a1 <= abscisse_souris() <= a1 + a) and (b1 <= ordonnee_souris() <= b1 + b):
        
        print ("ahah tu veux changer les parametres fdp ?")
    if (a2 <= abscisse_souris() <= a2 + a) and (b2 <= ordonnee_souris() <= b2 + b):
        print ("ahah tu veux jouer fdp ?")
    if (a3 <= abscisse_souris() <= a3 + a) and (b3 <= ordonnee_souris() <= b3 + b):
        print ("Ahah tu veux quitter le jeu fdp ?")
        QuitGame()

cree_fenetre(1000, 1000)

image(500, 200, 'paquet.png')
texte(75, 400, 'Jouer', couleur='Blue', taille=30)
texte(75, 600, 'Parametres', couleur='Blue', taille=30)
texte(75, 800, 'Quitter', couleur='Blue', taille=30)
mise_a_jour()

while True:
    mise_a_jour()
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == 'Quitte':
        QuitGame()

    print(zone_clic((75,600), (75, 400), (75, 800), 'Parametre'))




lst = create_game(5)
for i, elem in enumerate(lst):
    image(10, 10 + 30*i, 30, 30*i, 'allumerlefeu.png', tag='alumette')

