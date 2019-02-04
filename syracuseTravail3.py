# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 03:34:11 2019

@author: user
"""

# Permet decalculer les éléments d'une conjecture de Syracuse

import time
begin_time = time.time()
i = 1
syrac = list()
syrac.append("")
syrac.append(0)

def syracuse(n):
    cpt = 0 #compteur pour le nombre d'étape avant d'arriver à 1
    
    while (n!=1):
        if (n < len(syrac)): #Si le n courant est déjà calculé
            syrac.append(cpt + syrac[n])
        else:
            if (n%2 == 0):
                n = n/2
            else:
                n = (n*3)+1
        cpt = cpt + 1
        syrac.append(cpt)
    
    return syrac



while(time.time() - begin_time <= 0.001):
    print(syracuse(i))
    i = i+1