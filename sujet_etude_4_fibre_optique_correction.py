# coding: utf-8 
import math

# Structure de donnée
lst1 = [0.8891, 1.7741, 3.7495]
lst2 = [0.8891, 1.7741, 3.7495, 4.9005, 2.5555]

# Fonctions
""" Réaliser la fonction coefficient_attenuation() prenant
en paramètre une puissance de sortie mesurée sur une fibre
optique, et retournant le coefficient d’atténuation correspondant. """
def coefficient_attenuation(p_s):
    return 2*math.log10(5.0/p_s)

# Procédures traitants des fibres FO1, FO2 et FO3
""" Réaliser la procédure afficher() prenant en paramètre
les puissances de sortie des fibres FO1, FO2 et FO3, et
affichant ces puissances de sortie. """
# lst = [FO1, FO2, FO3]
def afficher(lst):
    print(lst[0])
    print(lst[1])
    print(lst[2])

""" Réaliser une procédure prenant en paramètre les puissances
de sortie des fibres FO1, FO2 et FO3, et affichant les coefficients
d’atténuations correspondants à ces puissances de sortie. """
def coeff_a(lst):
    print(coefficient_attenuation(lst[0]))
    print(coefficient_attenuation(lst[1]))
    print(coefficient_attenuation(lst[2]))

# Procédures traitants d’un ensemble de fibres
""" Réaliser la procédure afficher2() prenant en paramètre les
puissances de sortie d’un ensemble de fibres, et affichant ces
puissances de sortie. """
def afficher2(lst):
    n = len(lst)
    for i in range(n):
        print(lst[i])

""" Réaliser une procédure prenant en paramètre les puissances
de sortie d’un ensemble de fibres, et affichant les coefficients
d’atténuations correspondants à ces puissances de sortie. """
def coeff_a2(lst):
    n = len(lst)
    for i in range(n):
        print(coefficient_attenuation(lst[i]))

# Test
afficher(lst1)
coeff_a(lst1)
print("")
afficher2(lst2)
coeff_a2(lst2)
