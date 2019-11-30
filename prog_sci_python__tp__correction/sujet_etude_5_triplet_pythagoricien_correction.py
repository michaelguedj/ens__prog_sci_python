"""
    Sujet d’étude 5 : triplet pythagoricien
"""
import fractions
import math

# 1 -- type de donnée
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
# ou simplement 3 variables:
x1 = 1
y1 = 2
z1 = 3

x2 = 3
y2 = 4
z2 = 5

# 2 --
def pgcd(a, b):
    res = fractions.gcd(a, b)
    return res

# 3 --
def pgcd3(a, b, c):
    res = pgcd(pgcd(a, b), c)
    return res

# 4 --
def est_pythagoricien(a, b, c):
    if a**2+b**2==c**2:
        return True
    else:
        return False

# 5 --
def est_primitif(a, b, c):
    if pgcd3(a, b, c) == 1 and\
       est_pythagoricien(a, b, c) == True:
        return True
    else:
        return False

# 6 --
def generer1(n):
    for i in range(1, n):
        tmp = math.sqrt(2*i**2)
        print(i, i, tmp) 

# 7 --
def generer2(n):
    for i in range(1, n):
        for j in range(1, n):
            tmp = math.sqrt(i**2+j**2)
            print(i, j, tmp)

# 8 --
def generer3(n):
    for i in range(1, n):
        for j in range(1, n):
            tmp = math.sqrt(i**2+j**2)
            if est_primitif(i, j, tmp)==True:
                print(i, j, tmp)


"""
La solution precedante peut accepter
des triplets non entiers ;  
en effet, la condition :
    int(tmp) == tmp:
permet de vérifier que le flottant tmp
est bien un entier sur le plan mathématique
(par exemple : 1.0 est un entier).
"""

# 6 --
def generer1_bis(n):
    for i in range(1, n):
        tmp = math.sqrt(2*i**2)
        if int(tmp) == tmp:
            print(i, i, tmp) 

# 7 --
def generer2_bis(n):
    for i in range(1, n):
        for j in range(1, n):
            tmp = math.sqrt(i**2+j**2)
            if int(tmp) == tmp:
                print(i, j, tmp)

# 8 --
def generer3_bis(n):
    for i in range(1, n):
        for j in range(1, n):
            tmp = math.sqrt(i**2+j**2)
            if int(tmp) == tmp:
                if est_primitif(i, j, tmp)==True:
                    print(i, j, tmp)


if __name__ == "__main__":
    print(est_pythagoricien(x1, y1, z1))
    print(est_pythagoricien(x2, y2, z2))
 
    input()
    generer2(10)

    input()
    generer2_bis(10)
