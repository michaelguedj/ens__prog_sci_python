

import math
sqrt = math.sqrt

class Complexe():

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def somme(self, c):
        res = Complexe(self.re + c.re, \
                      self.im + c.im)
        return res

    def oppose(self):
        res = Complexe(-self.re, \
                       -self.im)
        return res    

    def est_imaginaire_pur(self):
        return self.re == 0

    def conjugue(self):
        res = Complexe(self.re, \
                       -self.im)
        return res
    
    def module(self):
        return sqrt(self.re**2 + self.im**2)

    def multiplication(self, c):
        res = Complexe(0, 0)
        res.re = self.re*c.re - self.im*c.im
        res.im = self.re*c.im - self.im*c.re
        return res
        
    # pour l'impression
    def __str__(self):
        res = str(self.re)
        res += " + "
        res += str(self.im) + ".i"
        return res

if __name__ == "__main__":
    c1 = Complexe(4, 3)
    c2 = Complexe(0, 1)
    print(c1)
    print(c2)
    print(c1.somme(c2))
    print(c1.oppose())
    print(c1.est_imaginaire_pur())
    print(c2.est_imaginaire_pur())
    print(c1.conjugue())
    print(c1.module())
    print(c1.multiplication(c2))
