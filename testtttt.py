from fltk import *

cree_fenetre(600, 600)
while True:

    ev = donne_ev()
    tev = type_ev(ev)

    if tev == 'ClicGauche':
        couple = abscisse_souris(), ordonnee_souris()
        print(couple)

    
    mise_a_jour()
    