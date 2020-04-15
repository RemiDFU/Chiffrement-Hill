#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:03:34 2019

@author: dfr2867a
"""
from numpy import*
import matplotlib.pyplot as plt
from pickle import *
import numpy as np
from scipy import optimize




#Question 1
fichier= open("data2.txt", "r")
x=load(fichier)
fichier.close()

nbCommunes = x.shape[0]

#Question 2
print 'Il y a',nbCommunes, 'communes en France'
nbHab = np.sum(x)
print'Il y a ',nbHab, 'habitants en France' 
minPop= np.min(x)
print 'La commune la moins peuplée a', minPop, 'habitant'
maxPop= np.max(x)
print 'La commune la plus peuplée a', maxPop, 'habitants'
moyenneNbHab = nbHab / nbCommunes
print'La moyenne habitant par ville en France est de',moyenneNbHab


def mediane(x):
    x.sort()
    N = len(x)
    n = N/2.0
    p = int(n)
    if n == p:
        return (x[p-1]+x[p])/2.0
    else:
        return L[p]
print 'La médiane de la population des communes en France est de', mediane(x)



moyenneNbHabcarre= moyenneNbHab*moyenneNbHab
xcarre = x*x
#Variance
variance = sum(xcarre)/x.shape[0] - moyenneNbHabcarre
print 'La variance de x est',variance

# Ecart type 
ecarttype= sqrt(variance)
print 'L''ecart-type de x est de',ecarttype





plt.hist(x)
plt.title('Histogramme', fontsize=10)
plt.savefig("plot_simple_histogramme_matplotlib_02.png")
plt.show()
#---------------------------------------------------------------------------------------
#Question 3
plt.hist(x, log=True, range=(minPop,maxPop-2))
plt.title('Histogramme', fontsize=10)
plt.savefig("plot_simple_histogramme_matplotlib_02.png")
plt.show()


