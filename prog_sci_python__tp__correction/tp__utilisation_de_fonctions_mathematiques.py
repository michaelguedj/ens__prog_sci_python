# -*- coding: utf-8 -*-
"""
    Utilisation de fonctions mathematiques
"""


from math import *


#- 1
print("\n\n  Exercice 1")
print("sin(pi)-cos(pi)=", sin(pi)-cos(pi))
print("sin(pi/2)-cos(pi/2)=", sin(pi/2)-cos(pi/2))
print("cos(pi)=", cos(pi))
print("cos(pi+2*pi)=", cos(pi+2*pi))
print("cos(5)=", cos(5))
print("cos(sqrt(5))=", sqrt(cos(5)))


#- 2
print("\n\n  Exercice 2")
def f(x,y):
    return sin(x)-cos(y)

print("f(pi, pi)=", f(pi, pi))
print("f(pi/2, pi)=", f(pi/2, pi))


#- 3
print("\n\n  Exercice 3")
print("2*sqrt(2)+2=", 2*sqrt(2)+2)
print("2*sqrt(2+2)=", 2*sqrt(2+2))
print("(3**3+3**5)/2 + sqrt(3)=", (3**3+3**5)/2 + sqrt(3))


#- 4
print("\n\n  Exercice 4")
def f(x,y,z):
    return (x**2+sqrt(y+2)+cos(z))/3

print("f(2, -2, pi)=", f(2, -2, pi))


#- 5
print("\n\n  Exercice 5")
print("2*ln(2)+3=", 2*log(2)+3)
print("2*log(2)+3=", 2*log10(2)+3)
print("2*log2(2)+3=", 2*log2(2)+3)


#- 6
print("\n\n  Exercice 6")
def f(x):
    return (2*log10(x)+3)/5

print("f(10)=", f(10))


#- 7
print("\n\n  Exercice 7")
def g(x,y):
    return (2*log10(x))/5 + y

print("g(10, 7)=", g(10, 7))
print("g(10, 8)=", g(10, 8))
print("g(10, 501)=", g(10, 501))


#- 8
print("\n\n  Exercice 8")
print("exp(3)=", exp(3))
print("exp(3/2)=", exp(3/2))
print("exp(ln(301))=", exp(log(301)))
print("10**log(501)=", 10**log10(501))

#- 9
print("\n\n  Exercice 9")
def toto(x):
    return 3*log((x+2)/5)

def tata(y):
    return 5*exp(y/3)-2

print("toto(tata(5))=", toto(tata(5)))
print("tata(toto(5))=", tata(toto(5)))

print("toto(tata(101))=", toto(tata(101)))
print("tata(toto(101))=", tata(toto(101)))
