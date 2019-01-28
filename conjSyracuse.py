# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:31:46 2019

@author: user
"""

# Permet decalculer les éléments d'une conjecture de Syracuse

import time
begin_time = time.time()
#n = int(input('Entrez un nombre'))
i = 1

def syracuse(n):
    syrac = list()
    syrac.append(n)
    while (n!=1):
        if (n%2 == 0):
            n = n/2
        else:
            n = (n*3)+1
        syrac.append(n)
    
    dico={}
    dico['liste']=syrac
    dico['longueur syrac'] = len(syrac)
    return dico

while(time.time() - begin_time <= 600):
    print(syracuse(i))
    i = i+1

print(i)

#1525454 : 257 étape avant d'arriver à 1.
#1525414 : 288

    #print si beaucoup d'éléments (x>300 ?) 
    # idée de "met longtemps à conver vers 4-2-1"