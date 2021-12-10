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
    [1, 2, 3, 4, 5]
    """
    
    if tev == 'ClicGauche':
        efface_tout()
        lst = []
        for i in range(nb_alum):
            alumettes = image(20 + 30*i, 80, 'allumerlefeu.png')
            lst.append(alumettes)
    
        return lst
    

def retrait_alum(lst):
    """
    """

    if len(lst) > 0:
        efface(lst.pop())

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
        texte(10,10, f"C'est au tour du joueur {cmpt} ", couleur='Blue', taille=20, tag="Joueur")
    else:

        cmpt += 1
        texte(10,10, f"C'est au tour du joueur {cmpt} ", couleur='Blue', taille=20, tag="Joueur")

    return cmpt


def zone_clic(abscisse, ordonnee, clicordo, clicabs):
    if abscisse == 



if __name__ == "__main__":
    ev = donne_ev()
    tev = type_ev(ev)

    







