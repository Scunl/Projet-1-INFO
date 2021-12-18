from fltk import *

lst = ["alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette", "alumette"]
nb_coup = 0

def create_game(nb_alum):
    """
    >>> create_game(5)
    [alumette, alumette, alumette, alumette, alumette]
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


def joue_coup(lst, coup, rang):
    eff = []
    for i in range(coup):
        eff.append(lst[rang].pop())
    return eff



def victoire(lst,coup):
    None

def menu():

    cree_fenetre(1920, 1080)

    image(960, 200, 'paquet.png', ancrage='center')
    image(100, 400, 'Jouer.png', ancrage='nw')
    image(100, 600, 'Settings.png', ancrage='nw')
    image(100, 800, 'exit.png', ancrage='nw')
    mise_a_jour()

    while True:
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        ### CREATION MAIN MENU ###
        if tev == 'Touche':
            efface_tout()
            image(960, 200, 'paquet.png', ancrage='center')
            image(100, 400, 'Jouer.png', ancrage='nw')
            image(100, 600, 'Settings.png', ancrage='nw')
            image(100, 800, 'exit.png', ancrage='nw')

        break

def jeu():
    while True:
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'ClicGauche':
        
            if zone_clic_menu((100, 400), 'Jouer.....'):
                efface_tout()
                lst = create_game(21)
                for i, elem in enumerate(lst):
                    image(50 + (50*i), 200, 'allumerlefeu.png', tag=f"alumette{i}")
        break
    


def QuitGame():
    """
    """
    exit()

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

cree_fenetre(1920, 1080)

image(960, 200, 'paquet.png', ancrage='center')
image(100, 400, 'Jouer.png', ancrage='nw')
image(100, 600, 'Settings.png', ancrage='nw')
image(100, 800, 'exit.png', ancrage='nw')
mise_a_jour()

if __name__ == '__main__':

    ### INTERFACE JEU ###
    while True:
            
            ### INTERFACE MENU ###
            

            
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'ClicGauche':
            if zone_clic_menu((100, 400), 'Jouer.....'):
                nb_coup = 0
                efface_tout()
                lst = create_game(21)
                for i, elem in enumerate(lst):
                    image(50 + (50*i), 200, 'allumerlefeu.png', tag=f"alumette{i}")
        break
    while True:

        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == 'ClicGauche':
            if retrait_alum(lst) == "il reste des alu":
                nb_coup += 1
                if nb_coup >=3:
                    texte(400, 400, "Vous avez atteint le maximum d'allumettes selectionnables", couleur='Red')

                ### CREATION MAIN MENU ###


    
        ### ENTRANCE: PLAY, SETTINGS, QUIT ###

            if retrait_alum(lst) == "pas d'alu":
                texte(960, 20, "Il n'y a plus d'alumette fils de pute", couleur='RED')

            if zone_clic_menu((100, 600), 'Parametres........'):
                efface_tout()
                texte(500, 50, 'Configuration des parametres:', taille=20, couleur='Red')
            if zone_clic_menu((100, 800), "Quitter....."):
                QuitGame()









if tev == 'Touche':
    efface_tout()
    image(960, 200, 'paquet.png', ancrage='center')
    image(100, 400, 'Jouer.png', ancrage='nw')
    image(100, 600, 'Settings.png', ancrage='nw')
    image(100, 800, 'exit.png', ancrage='nw')
