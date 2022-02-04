import random

def jouer_lievre_tortue():
    distance = 6
    position_tortue = position_lievre = 0
    resultat = random.randint(1,6)
    
    while position_lievre < 6 or position_tortue < 6:
        resultat = random.randint(1,6)
        if resultat != 6:
            position_tortue += 1
        else:
            position_lievre += 6
    
    if position_tortue == 6:
        return("tortue")
    else:
        return("lievre")


#TEST JEU LIEVERE & TORTUE

gain_tortue = 0
gain_lievre = 0

choix_range = 1000

for i in range(choix_range):
    resultat = jouer_lievre_tortue()
    
    if resultat == "tortue":
        gain_tortue += 1
    else:
        gain_lievre += 1

print(f"Le lievre a gagne {gain_lievre} fois et la tortue {gain_tortue} fois. Soit {int(gain_tortue / choix_range * 100)}% de victoire pour la tortue.")
