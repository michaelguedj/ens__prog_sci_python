
"""
    TP – Opérations sur points
"""

import math
sqrt = math.sqrt

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norme(self):
        return sqrt(self.x**2 + self.y**2)

    def produit_scalaire(self, p):
        return self.x * p.x + self.y * p.y

    def addition(self, p):
        return Point(self.x + p.x, \
                     self.y + p.y)

    def distance(self, p):
        return sqrt(
            (self.x - p.x)**2 +
            (self.y - p.y)**2)

    
    def __str__(self):
        return "("+\
               str(self.x)+", "+\
               str(self.y)+\
               ")"


if __name__ == "__main__":

    p1 = Point(5, 2)
    print(p1)
    print("norme:")
    print(p1.norme())
    print()
    
    p2 = Point(3, 4)
    print(p2)
    print("norme:")
    print(p2.norme())
    print()

    print("p1.p2")
    print(p1.produit_scalaire(p2))
    print()

    print("d(p1, p2)")
    print(p1.distance(p2))
    print()
    
    p3 = p1.addition(p2)
    print(p3)

