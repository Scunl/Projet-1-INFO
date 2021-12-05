from fltk import *

lst = ["alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette"]

def jeu(nb_alum, retrait):
    """
    Gagnant du jeu avec nombre donné d'alumette à retirer en fonction du nombre d'alumettes totales
    """

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

def create_game(nb_alum):
    """
    >>> create_game(5)
    [1, 2, 3, 4, 5]
    """
    cree_fenetre(1000, 1000)
    
    a = 3
    lst = []
    for i in range(nb_alum):
        rectangle(10 + 10*a*i, 100, 30 + 10*a*i, 200, couleur='Orange', remplissage='Orange')
        alumettes = rectangle(10 + 10*a*i, 100, 30 + 10*a*i, 200, couleur='Orange', remplissage='Orange')
        lst.append(alumettes)
    attend_ev()
    ferme_fenetre()
    lstf = []
    for elem in lst:
        lstf.append(int(elem/2))

    return lstf, lst

def retrait_alum(lst):
    """
    """
    while len(lst) > 0:
        
        attend_clic_gauche()
        lst.pop(0)
        efface(lst[0])




create_game(20)
retrait_alum(lst)


