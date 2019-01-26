# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:31:46 2019

@author: user
"""

# Permet decalculer les éléments d'une conjecture de Syracuse

n = int(input('Entrez nu nombre'))


def syracuse(n):
    syrac = list["",n]
    while (n>1):
        if (n%2 == 0):
            n = n/2
        else:
            n = (n*3)+1
        syrac.append(n)
    
    dico={}
    dico['liste']=syrac
    dico['longueur syrac'] = len(syrac)
    return dico

syracuse(n)