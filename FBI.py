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

def QuitGame():
    """
    """
    exit()

def zone_clic_menu(bouton1, bouton2, bouton3, text):
    """
    """


    a, b = taille_texte(text)
    a1, b1 = bouton1
    a2, b2 = bouton2
    a3, b3 = bouton3

    if (a1 <= abscisse_souris() <= a1 + a) and (b1 <= ordonnee_souris() <= b1 + b):
        

        type1 = "Jeu"

        return type1

    if (a2  <= abscisse_souris() <= a1 + a) and (b2 <= ordonnee_souris() <= b2 + b):
        

        type1 = "Settings"

        return type1
        

    if (a3 <= abscisse_souris() <= a3 + a) and (b3 <= ordonnee_souris() <= b3 + b):
        
        QuitGame()

    return None

    
    
    

def select(alumette):
    """
    """



if __name__ == '__main__':

    cree_fenetre(1920, 1080)

    image(960, 200, 'paquet.png')
    texte(75, 400, 'Jouer', couleur='Blue', taille=30)
    texte(75, 600, 'Parametres', couleur='Blue', taille=30)
    texte(75, 800, 'Quitter', couleur='Blue', taille=30)
    mise_a_jour()

    

    while True:
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)

        ### CREATION MAIN MENU ###
        if tev == 'Touche':
            efface_tout()
            image(960, 200, 'paquet.png', ancrage='center')
            texte(75, 400, 'Jouer', couleur='Blue', taille=30)
            texte(75, 600, 'Parametres', couleur='Blue', taille=30)
            texte(75, 800, 'Quitter', couleur='Blue', taille=30)
            
        ### ENTRANCE: PLAY, SETTINGS, QUIT ###
        if tev == 'ClicGauche':
        
            if zone_clic_menu((75, 400), (75, 600), (75, 800), 'Jouer..') == "Jeu":
                efface_tout()
                lst = create_game(21)
                for i, elem in enumerate(lst):
                    image(50 + 60*i, 200, 'allumerlefeu.png', ancrage='center', tag=f"alumette{i}")
                    
            mise_a_jour()
            if tev == 'ClicGauche':
                if retrait_alum(lst) == "il reste des alu":
                    efface(lst.pop())

                if retrait_alum(lst) == "pas d'alu":
                    texte(960, 20, "Il n'y a plus d'alumette fils de pute", couleur='RED', ancrage='center')

                    
            if zone_clic_menu((75, 400), (75, 600), (75, 800), 'Parametre') == "Settings":
                efface_tout()
                texte(500, 50, 'Configuration des parametres:', taille=20, couleur='Red', ancrage='center')
