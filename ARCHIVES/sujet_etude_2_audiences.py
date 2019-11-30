# coding: utf-8 
import math

# Structure de donnée
lst = [10,25,30,1,0.9]

# Fonctions et procédures
""" Réaliser une fonction nb_telespectateurs() prenant en paramètre
un pourcentage de part de marché, et retournant le nombre de
téléspectateurs correspondant."""
# Nb_telespectateurs(X) = 161707,317×X (X est un pourcentage de part de marché) ;
def nb_telespectateurs(X):
    return 161707.317*X 

""" Réaliser une fonction part_de_marché() prenant en paramètre un
nombre de téléspectateurs, et retournant le pourcentage de part de
marché correspondant. """
#part_de_marché(Y) = 6,184x10^(-6)×Y (Y est nombre de téléspectateurs).
def part_de_marche(Y):
    return 6.184*10**(-6)*Y

# Procédures sur la structure de donnée demandée
""" Réaliser une procédure afficher() prenant en argument la structure
de donnée permettant de stocker une suite de parts de marché, et affichant
cette structure de donnée."""
def afficher(lst):
    print(lst)

""" Réaliser une procédure prenant en argument la structure de donnée
permettant de stocker une suite de parts de marché, et affichant le nombre de
téléspectateurs correspondant à chaque part de marché."""
def part_de_marche_liste(lst):
    n = len(lst)
    for i in range(n):
        print("\n"+str(nb_telespectateurs(lst[i]))+" "),

""" Réaliser une procédure prenant en argument la structure de donnée
permettant de stocker une suite de parts de marché, et affichant la part
de marché la plus haute ainsi que le nombre de téléspectateurs correspondant.
"""
def part_de_marche_max(lst):
    n = len(lst)
    if n==0:
        return
    maxi = lst[0]
    for i in range(n):
        if lst[i] > maxi:
            maxi = lst[i]
    print("part de marche max : " + str(maxi))

""" Réaliser une procédure prenant en argument la structure de donnée
permettant de stocker une suite de parts de marché, et affichant le nombre
de téléspectateurs correspondant à l’ensemble de ces parts de marché."""
def spectateurs_tot(lst):
    somme = 0
    n = len(lst)
    for i in range(n):
        somme += nb_telespectateurs(lst[i])
    print("spectateurs total : " + str(somme))


# Test
print(lst)
part_de_marche_liste(lst)
part_de_marche_max(lst)
spectateurs_tot(lst)
