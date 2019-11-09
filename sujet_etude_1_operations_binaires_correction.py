# coding: utf-8 
import math

# Opérations binaires
# Fonctions
""" Réalisez la fonction not() qui prend en argument un bit et
retourne sa négation. """
def non(b):
    if b == 0:
        return 1
    if b == 1:
        return 0

""" Réalisez la fonction or() qui prend en argument deux bits et
retourne leur disjonction. """
def ou(b1, b2):
    if b1 == 1:
        return 1
    if b2 == 1:
        return 1
    # sinon b1=0 et b2=0
    return 0
    
""" Réalisez la fonction and() qui prend en argument deux bits et
retourne leur conjonction. """
def et(b1, b2):
    if b1 == 0:
        return 0
    if b2 == 0:
        return 0
    # sinon b1=1 et b2=1
    return 1

# Opérations bits à bits sur les octets
# Structure de données
""" Déterminez la structure de donnée nécessaire pour stocker
un octet (8 bits). """
o1 = [1,0,0,1,1,1,1,0]
o2 = [1,1,1,1,0,0,0,0]


# Fonctions
""" Réalisez la fonction not_octet() qui prend en argument un
octet et retourne sa négation bit à bit. """
def non_oct(o):
    res = [0]*8
    for i in range(8):
        res[i] = non(o[i])
    return res

""" Réalisez la fonction or_octet() qui prend en argument deux
octets et retourne leur disjonction bit à bit. """
def ou_oct(o1, o2):
    res = [0]*8
    for i in range(8):
        res[i] = ou(o1[i], o2[i])
    return res

""" Réalisez la fonction and_octet() qui prend en argument deux
octets et retourne leur conjonction bit à bit. """
def et_oct(o1, o2):
    res = [0]*8
    for i in range(8):
        res[i] = et(o1[i], o2[i])
    return res

# Test
print(o1)
print(non_oct(o1))
print("")
print(o1)
print(o2)
print(ou_oct(o1,o2))
print("")
print(o1)
print(o2)
print(et_oct(o1,o2))
