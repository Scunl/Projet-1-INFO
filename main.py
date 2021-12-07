from fltk import *

lst = ["alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette"]
print("vous etes pas en mode misere")


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
    [1, 2, 3, 4, 5]
    """
    cree_fenetre(1000, 1000)
    image(500, 200, 'paquet.png')
    texte(100, 500, 'Jouer', couleur='Blue', taille=30)
    
    while True:
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == 'ClicGauche':
            efface_tout()
            lst = []
            for i in range(nb_alum):
                alumettes = image(20 + 30*i, 80, 'allumerlefeu.png')
                lst.append(alumettes)
        
        
        if tev =='ClicGauche':
            return lst
        if tev == 'Quitte':
            exit()
        
        
    

def retrait_alum(lst):
    """
    """

    a = []
    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'Quitte':
            exit()

        if len(lst) > 0:
            if tev == 'ClicGauche':
                efface(lst.pop())

        txt = texte(400, 400, "Au tour du joueur 1", couleur='black', taille=40)
        mise_a_jour()
        if tev == 'ClicDroit':
            efface(txt)
            mise_a_jour()
            txt = texte(100, 400, "Au tour du joueur 2", couleur='black', taille=40)
        
        mise_a_jour()
                

def tour_joueur(joueur):
    """
    """
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        
        texte(400, 400, "Au tour du joueur 1", couleur='black', taille=40)
        mise_a_jour()
        if tev == 'ClicDroit':
            texte(200, 400, "Au tour du joueur 2", couleur='black', taille=40)
        
        mise_a_jour()

print("vous etes pas en mode misere")
retrait_alum(create_game(20))


