import random

#CREATION DE LA FONCTION POUR TROUVER LE NOM DU PEUPLE#

def nom_du_peuple():
    random_number = random.randint(0,4)   
    if random_number == 1 :
        print("Ce qui se passe ici reste ici")
    elif random_number == 2 :
        print("")
    elif random_number == 3 :
        print("3")
    elif random_number == 4 :
        print("4")
    

nom_du_peuple()