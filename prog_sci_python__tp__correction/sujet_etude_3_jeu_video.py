
"""
    Sujet d’étude 3 : tournoi de jeu vidéo
"""

# stockage des scores des joueurs d'une equipe
scores_1 = [2, 0, 21, -10, 10]
scores_2 = [0, 3, 30, -10, 5]


# retourne le nb de joueurs
def nb_joueurs(scores):
    n = len(scores) # length
    return n

# aucun joueur dans une equipe
def est_equipe_vide(scores):
    n = len(scores)
    if n == 0:
        return True
    else:
        return False


# afficher les scores >0
def afficher_scores_strict_positifs(scores):
    n = len(scores)
    for i in range(n): #i=0,..., n-1
        if scores[i] > 0:
            print(scores[i], end=" ")
    print()

# afficher les scores >= x
def afficher_scores_superieurs_x(scores, x):
    n = len(scores)
    for i in range(n):
        if scores[i] >= x:
            print(scores[i], end=" ")
    print()


# calcule la moyenne des scores d'une equipe
def moyenne(scores):
    n = len(scores)
    res = 0
    for i in range(n): 
        res += scores[i]
    return res/n

# calcule la variance des scores d'une equipe
def variance(scores):
    n = len(scores)
    res = 0
    mu = moyenne(scores)
    for i in range(n): #i=0,..., n-1
        res = (scores[i]-mu)**2
    return res/n


print(scores_1)
print(scores_2)

print("\n---")
afficher_scores_strict_positifs(scores_1)
afficher_scores_strict_positifs(scores_2)

print("\n---")
afficher_scores_superieurs_x(scores_1, 10)
afficher_scores_superieurs_x(scores_2, 10)

print("\n---")
print("moyenne scores_1 :", moyenne(scores_1))
print("moyenne scores_2 :", moyenne(scores_2))

print("variance scores_1 :", variance(scores_1))
print("variance scores_1 :", variance(scores_2))
