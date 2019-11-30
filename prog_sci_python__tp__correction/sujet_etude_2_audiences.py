# coding: utf-8 

"""
    Sujet d’étude 2 : audiences
"""

# Structure de donnée
lst = [28.2/100, 25.5/100, 10.6/100, 7.7/100, 4.1/100]


def nb_telespectateurs(X):
    return 142375.89*X*100

def part_de_marche(Y):
    return 7.02*10**(-6)*Y

def afficher(lst):
    print(lst)

def nb_each(lst):
    n = len(lst)
    for i in range(n):
        print(nb_telespectateurs(lst[i]))

def part_de_marche_max(lst):
    n = len(lst)
    if n==0:
        return
    maxi = lst[0]
    for i in range(n):
        if lst[i] > maxi:
            maxi = lst[i]
    print("part de marche max : ", maxi)

def spectateurs_tot(lst):
    somme = 0
    n = len(lst)
    for i in range(n):
        somme += nb_telespectateurs(lst[i])
    print("spectateurs total :", somme)

def spectateurs_tot__bis(lst):
    print(nb_telespectateurs(sum(lst)))


if __name__ == "__main__":
    print(lst)
    nb_each(lst)
    part_de_marche_max(lst)
    spectateurs_tot(lst)
    spectateurs_tot__bis(lst)
