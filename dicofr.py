mots_fr = []
mots_cherches = []


dicofr = open("dico_utf8.txt", "r")
print(dicofr)
"""liste_mots_fr = dicofr.readlines()
for i in liste_mots_fr:
    mots_fr.append(i.replace("\n", ""))



def recherche(dico):
    start = input("Premiere lettre du mot: ")
    longueur = input("Longueur du mot: ")
    lettres = input("lettres dans le(s) mot(s): ")
    for i in dico:
        if i[0] == start and len(i) == int(longueur) and lettres in i:
            mots_cherches.append(i)
        elif len(i) == int(longueur) and lettres in i:
            mots_cherches.append(i)


recherche(mots_fr)
print(mots_cherches)"""