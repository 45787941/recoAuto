# Resoud l'exo du 08/10/18
# Trouve toutes les permutations possibles de la distributions du VECTEUR
# d'observation sur les 3 etats d'un hmm
# calcul simplifie de l'expo de la densité de proba, pour trouver si
# on observe un OUI ou un non

#####
# COLLOT Kevin
# M2 INFO DID - UTLN
# 2018/2019
#####

import itertools

P_oui = [2, 4, 3]
P_non = [3, 2, 1]
observations = [1, 2, 2, 2, 2, 3, 3]


def main(listObs, permutation):
    global P_oui, P_non
    resOui = pow(listObs[0] - P_oui[0], 2) + pow(listObs[-1] - P_oui[2], 2)
    resNon = pow(listObs[0] - P_non[0], 2) + pow(listObs[-1] - P_non[2], 2)

    i = 1
    j = 0
    while i < len(listObs) - 1:
        resOui += pow(listObs[i] - P_oui[int(permutation[j]) - 1], 2)
        resNon += pow(listObs[i] - P_non[int(permutation[j]) - 1], 2)
        i += 1
        j += 1

    return resOui, resNon

def DistribEtat(nbObs):
    """ Genere la liste de toutes les permutations possibles (même les mauvaises)
    de la distributions des observations sur les 3 états """
    listePossibilite = []
    i = 0
    for i in itertools.product("123", repeat=nbObs):
        listePossibilite.append(list(i))
    return listePossibilite

def FiltreListe(listePossibilite):
    """ SUpprime les permutations incorrectes"""
    i = 0
    while i < len(listePossibilite):
        if '2' not in listePossibilite[i]:
            listePossibilite.pop(i)
        else:
            i += 1
    i = 0
    while i < len(listePossibilite):
        if sorted(listePossibilite[i]) != listePossibilite[i]:
            listePossibilite.pop(i)
        else:
            i += 1
    return listePossibilite

def RechercheMin(listRes):
    """ Recherche des valeurs min du oui et du non """
    minOui = listRes[0][0]
    minNon = listRes[0][1]

    i = 1
    while i < len(listRes):
        if(listRes[i][0] < minOui):
            minOui = listRes[i][0]
        if(listRes[i][1] < minNon):
            minNon = listRes[i][1]
        i += 1
    return minOui, minNon


if __name__ == '__main__':
    print("######### VECTEUR D'OBSERVATION #########")
    print(observations)

    listeCpt = DistribEtat(len(observations)- 2)

    print("######### LISTE DES PERMUTATIONS #########")
    listFiltree = FiltreListe(listeCpt)
    print(listFiltree)
    print("Total " + str(len(listFiltree)) + " permutations correctes")

    listRes = []
    for i in range(0, len(listFiltree)):
        listRes.append(main(observations, listFiltree[i]))
    print("######### LISTE DES PROBABILITES (OUI, NON) #########")
    print(listRes)
    print("Total " + str(len(listRes)) + " couples de probas calculés ")

    print("######### AFFICHAGE DE Poui min et Pnon min #########")
    a, b = RechercheMin(listRes)
    print("P(oui) minimum = " + str(a))
    print("P(non) minimum = " + str(b))

    print("######### REPONSE #########")
    if a < b:
        print("Doit être un OUI (" + str(a) + " < " + str(b) + ")")
    elif b < a:
        print("Doit être un NON (" + str(b) + " < " + str(a) + ")")
    else:
        print("Peut être un OUI ou un NON (" + str(a) + " = " + str(b) + ")")
