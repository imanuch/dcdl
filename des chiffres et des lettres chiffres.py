from random import choice
from random import randint
from math import *
import time
debut = time.time()
def calculs(a,i,j,n):
    liste = []
    for nbr in range(len(a)):
        liste.append(a[nbr])

    if n == 0:
        liste.append(liste[i]*liste[j])
        del liste[j]
        del liste[i]

    elif n == 1 and liste[j]!=0:
        liste.append(liste[i]/liste[j])
        del liste[j]
        del liste[i]

    elif n == 2:
        liste.append(liste[i]+liste[j])
        del liste[j]
        del liste[i]
    elif n == 3:
        liste.append(liste[i]-liste[j])
        del liste[j]
        del liste[i]
    elif n == 4:
        liste.append(liste[j]-liste[i])
        del liste[j]
        del liste[i]
    elif n == 5 and liste[i]!=0:
        liste.append(liste[j]/liste[i])
        del liste[j]
        del liste[i]
    return liste


def chiffres(n,liste):
    cal = ["*","/","+","-","-","/"]
    if n in liste:
        return True
    if 0 in liste:
        return False
    for i in range(len(liste)-1):
        for j in range(i+1,len(liste)):
            for k in range(6):
                if chiffres(n,calculs(liste,i,j,k)):
                    if k<4:
                        print(liste,liste[i],cal[k],liste[j]," = ",calculs(liste,i,j,k)[-1])
                    else:
                        print(liste,liste[j],cal[k],liste[i]," = ",calculs(liste,i,j,k)[-1])
                    return True
    return False

#chiffres(848,[3,8,50,6,25,8])
chiffres(491,[25,4,4,8,1,50])
# chiffres(112,[9,6,7,3,1,7])
#chiffres(328,[2,17,5,556,326,12,99,9,84])