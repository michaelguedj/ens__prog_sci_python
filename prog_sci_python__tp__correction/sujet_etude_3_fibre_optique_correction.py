# coding: utf-8 
import math

"""
    Sujet d’étude 3 : fibre optique
"""

log10 = math.log10

# Structure de donnée
lst1 = [0.8891, 1.7741, 3.7495]
lst2 = [0.8891, 1.7741, 3.7495, 4.9005, 2.5555]

# Fonctions
def coefficient_attenuation(p_s):
    return 2*log10(5.0/p_s)

# Procédures traitants des fibres FO1, FO2 et FO3
# lst = [FO1, FO2, FO3]
def afficher(lst):
    print(lst[0])
    print(lst[1])
    print(lst[2])
    print("")

def coeff_a(lst):
    print(coefficient_attenuation(lst[0]))
    print(coefficient_attenuation(lst[1]))
    print(coefficient_attenuation(lst[2]))

# Procédures traitants d’un ensemble de fibres
def afficher2(lst):
    n = len(lst)
    for i in range(n):
        print(lst[i])
    print("")

def coeff_a2(lst):
    n = len(lst)
    for i in range(n):
        print(coefficient_attenuation(lst[i]))


if __name__ == "__main__":
    afficher(lst1)
    coeff_a(lst1)
    print("---")
    afficher2(lst2)
    coeff_a2(lst2)

    
