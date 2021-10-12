#!/usr/bin/python3
def decrypt(texte, decalage):
    """Renvoie une chaine de caractères décalés
 
        Attend une chaîne de caractères non accentués
        éventuellement vide : texte
 
        Un entier positif entre 0 et 25 : decalage
         
        Renvoie une chaîne de la même longueur avec des caractères
        décalés de ... decalage, et ramenés dans l'alphabet
        en revenant de 26si on dépasse z ou Z
 
        Garde les caractères non alphabétiques
    """
         
    # Une chaîne vide à compléter au fur et à mesure
    resultat = ""
 
    # On parcourt la chaîne texte
    for lettre in texte:
 
        # décalage -> new est un code ASCII
        new = ord(lettre) + decalage
         
        if 65 <= ord(lettre) <= 90:    # si minuscule
            if new > 90:               # dépassement du z ?
                new -= 26
            resultat += chr(new)        # on rajoute le caractère décalé
        elif 97 <= ord(lettre) <= 122: # si majuscule
            if new > 122:              # dépassement du Z ?
                new -= 26
            resultat += chr(new)        # on rajoute le caractère décalé
        else:
            resultat += lettre   # on rajoute le caractère non décalé
 
    # On renvoie la nouvelle chaîne
    return resultat


mot = "TIPGKFXIRGYZV RMRETVV"

for d in range(1,26):
    print("Décalage #%d : %s" % (d, decrypt(mot, d)))
