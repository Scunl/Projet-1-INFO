from tkinter.constants import Y
from fltk import *
from time import sleep

# PROPRIETE DE WALID
# NE PAS LIRE (illégal)
n = 21
nombre_max = 3

def create_game(nb_alum):
    """
    """
    
    lst = []
    for i in range(nb_alum):
        
        lst.append(f"alumette{i}")

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
    eff = []
    for i in range(coup):
        eff.append(lst.pop())
    return eff



def victoire(lst):
    """
    """
    if len(lst) == 0 :              
        if cmpt == 1:
            a = "j1"
        if cmpt == 2:
            a = "j2"
    else:
        return False

    return a 



def zone_clic_menu(bouton, text):
    """
    """


    a, b = taille_texte(text)
    a1, b1 = bouton

    if (a1 <= abscisse_souris() <= a1 + a) and (b1 <= ordonnee_souris() <= b1 + b):
        return True

    return False

    



    

def select(alumette):
    """
    """

x = 1080
y = 960

cree_fenetre(x, y)

image(x/2, y/6, 'paquet.png', ancrage='center')
image(x/10, y/4, 'Jouer.png', ancrage='nw')
image(x/10, y/3, 'Settings.png', ancrage='nw')
image(x/10, y/2, 'Quitter.png', ancrage='nw')
mise_a_jour()


if __name__ == '__main__':
    
    
    while True:
        
        
    ### INTERFACE MENU ###
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        
        if tev == 'Quitte':
            exit()

        if tev == 'ClicGauche':

            mise_a_jour()
            if zone_clic_menu((100, 800), "Quitter....."):
                exit()

            if zone_clic_menu((x/10, y/4), 'Jouer.....'):
                break

            if zone_clic_menu((x/10, y/3), 'Parametres........'):
                efface_tout()
                texte(x/2 - len("Configuations des parametres") - 20, y//10, "Configuations des parametres")
                texte(x//6, y//4, "-")
                texte(x//4, y//4, str(n), tag="n")
                texte(x//3, y//4, "+")
                image(x//4, y/2, "Jouer.png", ancrage="nw")

                while True:
                    mise_a_jour()
                    ev = donne_ev()
                    tev = type_ev(ev)

                    if tev == 'Quitte':
                        exit()
                    if tev == 'ClicGauche':
                        if zone_clic_menu((x//6, y//4), "Moin"):
                            n=n-1
                            if n <= 0:
                                n += 1
                                texte(x - (x/2), y/5, "T'es sûr tu veux jouer ?", tag="limit2")
                            efface("n")
                            texte(x//4, y//4, str(n), tag="n")
                        if zone_clic_menu((x//3, y//4), "Plus"):
                            efface("limit2")
                            n=n+1
                            if n > 40:
                                n -= 1
                            efface("n")
                            texte(x//4, y//4, str(n), tag="n")
                        if zone_clic_menu((x//4,y/2), "Jouer"):
                            break
                break
            


    ### INTERFACE JEU ###
    cmpt = 1
    nb_coup = 0
    efface_tout()
    lst = create_game(n)
    for i, elem in enumerate(lst):
        image(30 + (x/len(lst)*i - 20), 200, 'allumerlefeu.png', tag=f"alumette{i}")
    texte(x // 2, y // 20, f"C'est au tour du joueur 1", tag="j")

    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        
    
        if tev == 'Quitte':
            exit()


        if tev == 'ClicGauche':
            if retrait_alum(lst) == "il reste des alu":
                if nb_coup >= nombre_max or nb_coup >= len(lst):
                    texte(100, 70, "Vous avez atteint le maximum d'allumettes selectionnables", couleur='Red', tag="limit", taille=15)
                else:
                    efface("nbcoup")
                    nb_coup += 1
                    texte(x//2, y//2, str(nb_coup), tag='nbcoup')

        if tev == 'ClicDroit': 
            if nb_coup:
                efface("limit")
                efface("nbcoup")
                nb_coup-=1
                if nb_coup:
                    texte(x//2, y//2, str(nb_coup), tag='nbcoup')
        

        if tev == 'Touche':

            efface("limit")
            eff = joue_coup(lst, nb_coup)
            if nb_coup > 0:
                if cmpt == 1:
                    cmpt += 1
                else:
                    cmpt -= 1
                efface("j")
                texte(x // 2, y // 20, f"C'est au tour du joueur {cmpt}", tag="j")

            for elem in eff:
                efface(elem)

            efface("nbcoup")
            mise_a_jour()

            nb_coup = 0
            vic = victoire(lst)
            if victoire(lst):
                efface_tout()
                texte(x/2, y/2, f"Le joueur {vic} a gagné")


            

            

                ### CREATION MAIN MENU ###


    
        ### ENTRANCE: PLAY, SETTINGS, QUIT ###

