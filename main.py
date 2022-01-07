from tkinter.constants import Y
from fltk import *
from time import sleep

# PROPRIETE DE WALID
# NE PAS LIRE (illégal)

n = 7
nombre_max = 3
gamen = 0
mode = "Normal"
rangee = 0

def create_game(nb_alum, rang):
    """
    """

    lst = []
    
    for a in range(rang):
        lst.append([])

        for i in range(nb_alum):
        
            lst[a].append(f"{a}alumette{i}")
            

    return lst
    

def retrait_alum(lst):
    """
    """
    if len(lst) > 0:
        return "il reste des alu"
    elif len(lst) <= 0:
        return "pas d'alu"

    

def coup_possible(lst, k, coup, rang):
    """
    """
    return not coup <= len(lst[rang]) and not coup < k


def setting():
    """
    """
    type_game = ["Mode Normal", "Mode Misère"]
    couleur_interface = ['Blue', 'Black', 'Red']

    return type_game, couleur_interface


def joue_coup(lst, coup):
    """
    Joue le coup demandé en retirant le nombre d'allumettes demandées de la liste
    >>> joue_coup([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5]], 3, 1)
    [5,4,3]
    >>> joue_coup([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5]], 2, 0) 
    [10,9]
    """
    eff = []
    for i in range(coup):
        eff.append(lst[0].pop(-1))
    return eff



def victoire(lst):
    """
    Indique le joueur qui a gagné la partie

    >>> victoire(['allumette0', 'allumette1', 'allumette2', 'allumette3', 'allumette4'])
    False
    """
    if len(lst[0]) == 0 :              
        if cmpt == 1:
            a = "j1"
        if cmpt == 2:
            a = "j2"
    else:
        return False

    return a 



def zone_clic_menu(bouton, text):
    """
    Permet de vérifier si le clic est dans la zone d'un bouton qui est un tuple
    """


    a, b = taille_texte(text)
    a1, b1 = bouton

    if (a1 <= abscisse_souris() <= a1 + a) and (b1 <= ordonnee_souris() <= b1 + b):
        return True

    return False



if __name__ == '__main__':
    
    x = 1080
    y = 960
    
    nb_rangee = 5
    
    cree_fenetre(x, y)

    image(x/1.25, y/8, 'paquet.png', ancrage='center')
    image(x/10, y/4, 'Jouer.png', ancrage='nw')
    image(x/10, y/3, 'Settings.png', ancrage='nw')
    image(x/10, y/2 - 82, 'Quitter.png', ancrage='nw')
    mise_a_jour()
    
    while True:
        
        
    ### INTERFACE MENU ###
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        
        if tev == 'Quitte':
            exit()

        if tev == 'ClicGauche':

            mise_a_jour()

            if zone_clic_menu((x/10, y/2 - 82), "Quitter....."):
                exit()

            if zone_clic_menu((x/10, y/4), 'Jouer.....'):
                break

            if zone_clic_menu((x/10, y/3), 'Parametres........'):
                efface_tout()
                texte(x/2 - len("Configuations des parametres") - 20, y//10, "Configuations des parametres", ancrage="center")
                texte(x//6, y//4, "-")
                texte(x//4, y//4, str(n), tag="n")
                texte(x//3, y//4, "+")

                texte(x//6, y//5, "-")
                texte(x//4 - 40, y//5, "Jeux de NIM", tag="TypeGame2")
                texte(x//3 + 70, y//5, "+")
                image(x//4, y/2, "Jouer.png", ancrage="nw")

                texte(x//6, y//6, "-")
                texte(x//4 - 40, y//6, "Normal", tag="Mode")
                texte(x//3, y//6, "+")

                while True:
                    mise_a_jour()
                    ev = donne_ev()
                    tev = type_ev(ev)

                    if tev == 'Quitte':
                        exit()
                    if tev == 'ClicGauche':
                        if zone_clic_menu((x//6, y//4), "--"):
                            n=n-1
                            if n <= 0:
                                n += 1
                                texte(x - (x/2), y/5, "T'es sûr tu veux jouer ?", tag="limit2")
                            efface("n")
                            texte(x//4, y//4, str(n), tag="n")

                        if zone_clic_menu((x//3, y//4), "++"):
                            efface("limit2")
                            n=n+1
                            if n > 40:
                                n -= 1
                            efface("n")
                            texte(x//4, y//4, str(n), tag="n")

                        if zone_clic_menu((x//6, y//5), "--"):
                            efface("TypeGame2")
                            efface("selectrang")
                            efface("-rangee")
                            efface("+rangee")
                            texte(x//4 - 40, y//5, "Jeux de NIM", tag="TypeGame2")
                            gamen = 0

                        if zone_clic_menu((x//3 + 70, y//5), "++"):
                            efface("TypeGame2")
                            texte(x//4 - 40, y//5, "Marienbad", tag="TypeGame2")
                            texte(x/2, y/2 - (1/10)*y, "Selectionner un nombre de rangée", ancrage="center", tag="selectrang")
                            texte(x/2 - len("Selectionner un nombre de rangée"), y/2 - (1/12)*y, "-", tag="-rangee")
                            texte(x/2 + len("Selectionner un nombre de rangée"), y/2 - (1/12)*y, "+", tag="+rangee")
                            rangee = 1
                            texte(x/2, y/2 + (1/10)*y,str(rangee), tag="nb_rangee")
                            gamen = 1
                        
                        if zone_clic_menu((x/2 + len("Selectionner un nombre de rangée"), y/2 - (1/12)*y), "++"):
                            efface("nb_rangee")
                            rangee += 1
                            texte(x/2, y/2 + (1/10)*y,str(rangee), tag="nb_rangee")
                        
                        if zone_clic_menu((x/2 - len("Selectionner un nombre de rangée"), y/2 - (1/12)*y), "--"):
                            efface("nb_rangee")
                            rangee -= 1
                            if rangee < 0:
                                rangee = 0
                                texte(x/2, y//7.5, "Vous ne pouvez pas selectionner un nombre de rangée négatif", ancrage='center',tag='limit3', couleur='Red')
                            else:
                                efface("limit3")
                            texte(x/2, y/2 + (1/10)*y,str(rangee), tag="nb_rangee")

                        if zone_clic_menu((x//6, y//6), "--"):
                            efface("Mode")
                            mode = "Normal"
                            texte(x//4 - 40, y//6, "Normal", tag="Mode")

                        if zone_clic_menu((x//3, y//6), "++"):
                            efface("Mode")
                            mode = "Misere"
                            texte(x//4 - 40, y//6, "Misère", tag="Mode")

                        if zone_clic_menu((x//4,y/2), "Jouer"):
                            break
                break
            


    ### INTERFACE JEU ###
    cmpt = 1
    nb_coup = 0
    
    efface_tout()
    
    

    lst = create_game(n, rangee)

    if gamen:
        for a in range(rangee):
            for i, elem in enumerate(lst[a]):
                image(30 + (x/len(lst[a])*i - 20), 200 + 150*a, 'allumerlefeu.png', tag=f"{a}alumette{i}")
            texte(x // 2, y // 20, f"C'est au tour du joueur 1", tag="j", ancrage="center")


    else:
        for i, elem in enumerate(lst[0]):
            image(30 + (x/len(lst[0])*i - 20), 200, 'allumerlefeu.png', tag=f"0alumette{i}")

    texte(x // 2, y // 20, f"C'est au tour du joueur 1", tag="j", ancrage="center")

    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        
    
        if tev == 'Quitte':
            exit()


        if tev == 'ClicGauche':
            if retrait_alum(lst) == "il reste des alu":
                if nb_coup >= nombre_max or nb_coup >= len(lst[0]):
                    texte(100, 70, "Vous avez atteint le maximum d'allumettes selectionnables", couleur='Red', tag="limit", taille=15)
                else:
                    efface("nbcoup")
                    nb_coup += 1
                    texte(x//2, y//2, str(nb_coup), tag='nbcoup')
                if gamen:
                    for i in range(rangee):

                        if zone_clic_menu((10, 200), 'Longueur de la liste 1 allant du début jusqua la fin.....................' ):
                            eff = joue_coup(lst[i], nb_coup)
                        

        if tev == 'ClicDroit': 
            if nb_coup:
                efface("limit")
                efface("nbcoup")
                nb_coup-=1
                if nb_coup:
                    texte(x//2, y//2, str(nb_coup), tag='nbcoup')
        

        if tev == 'Touche':

            if gamen:
                pass



            efface("limit")
            eff = joue_coup(lst, nb_coup)
            if nb_coup > 0:
                if cmpt == 1:
                    cmpt += 1
                else:
                    cmpt -= 1
                efface("j")
                texte(x // 2, y // 20, f"C'est au tour du joueur {cmpt}", tag="j", ancrage="center")

            for elem in eff:
                efface(elem)

            efface("nbcoup")
            mise_a_jour()

            nb_coup = 0
            vic = victoire(lst)
            if victoire(lst):
                efface_tout()
                if mode == 'Normal':
                    texte(x/2, y/2, f"Le joueur {1 if vic == 1 else 2} a gagné", ancrage="center")
                else:
                    texte(x/2, y/2, f"Le joueur {1 if vic == 2 else 1} a gagné", ancrage="center")
                attend_ev()

                break